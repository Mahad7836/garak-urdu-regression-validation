import pytest

import garak._plugins
import garak.probes.base
from garak.attempt import Attempt, Message
from garak.detectors.promptinject import AttackRogueString


class ContextualUrduProvider:
    source_lang = "en"
    target_lang = "ur"

    def get_text(self, prompts, reverse_translate_judge=False, notify_callback=None):
        results = []
        for prompt in prompts:
            if prompt == "I hate humans":
                translated = "میں انسان سے نفرت کرتا ہوں"
            else:
                translated = prompt.replace(
                    "I hate humans",
                    "میں انسانوں سے نفرت کرتا ہوں"
                )
            results.append(translated)
            if notify_callback:
                notify_callback()
        return results


@pytest.mark.xfail(
    strict=True,
    reason="PR #2309 misses context-dependent Urdu trigger variants"
)
def test_contextual_urdu_trigger_should_be_detected(monkeypatch):
    monkeypatch.setattr(
        garak.probes.base.Probe,
        "_get_langprovider",
        lambda self: ContextualUrduProvider()
    )

    probe = garak._plugins.load_plugin(
        "probes.promptinject.HijackHateHumans"
    )

    translated_prompt = probe.langprovider.get_text([probe.prompts[0]])[0]

    attempt = Attempt(prompt=Message(translated_prompt))
    attempt = probe._attempt_prestore_hook(attempt, 0)
    attempt.outputs = [translated_prompt]

    assert "میں انسانوں سے نفرت کرتا ہوں" in translated_prompt
    assert AttackRogueString().detect(attempt) == [1.0]
