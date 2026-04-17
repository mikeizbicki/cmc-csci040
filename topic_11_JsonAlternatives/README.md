# Json Alternatives

<img width=300px src=img/yaml-json.jpg />

<!--
<img width=300px src=img/yaml-mask.jpg />
-->

<img width=300px src=img/toml.png />

## Notes

Quiz Wednesday on <https://github.com/mikeizbicki/quiz/blob/master/quiz_python_with_exceptions/topic11_config_formats.pdf>

Useful debugging tip: display the YAML/TOML config as JSON
```
import json
dump = json.dumps(data, indent=2)
print(dump)
```

**Fun links:**
1. "hard CS": new alternatives to JSON/XML/YAML/TOML:
    1. <https://github.com/toon-format/toon>
    1. <https://www.reddit.com/r/LocalLLaMA/comments/1pa3ok3/toon_is_terrible_so_i_invented_a_new_format_tron/>
    1. <https://tron-format.github.io/>
1. "soft CS": measuring developer productivity with LLMs:
    1. <https://arxiv.org/abs/2507.09089>
1. real CS happens in "weird" places:
    1. <https://www.theatlantic.com/technology/2026/04/4chan-ai-dungeon-thinking-reasoning/686794/>
    1. <https://www.lesswrong.com/posts/gpyqWzWYADWmLYLeX/how-ai-is-learning-to-think-in-secret>

## Lab

This is just a working period for you all.

Those of you who have submitted the project should have grades and a pull request with my detailed comments.
These include comments about:
1. why your grade is the way it is
1. stylistic comments about how to improve your code
1. any changes to make before the 2nd submission

I encourage you all to work through/merge this pr and ask me any clarifying questions.
