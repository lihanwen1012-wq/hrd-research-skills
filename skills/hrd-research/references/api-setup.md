# First-use API setup

Apply this workflow before the first article search in a conversation, or when the user requests API setup. Ordinary writing and revision do not require API keys. Downloading the skill alone does not run an installer or prompt; these instructions take effect when the agent uses it.

## Check availability privately

Check only whether each variable is present and nonempty in the process that will run the search helpers. Never print its value, dump the environment, or read secrets into conversational output. Report `configured` or `missing`; configured does not mean authenticated until a request succeeds. Do not make API requests merely to display setup status.

| Source | Environment variable | Request access |
| --- | --- | --- |
| Scopus | `SCOPUS_API_KEY` | https://dev.elsevier.com/ |
| Semantic Scholar | `SEMANTIC_SCHOLAR_API_KEY` | https://www.semanticscholar.org/product/api |
| Web of Science Starter | `WOS_API_KEY` | https://developer.clarivate.com/apis/wos-starter |

Each user supplies their own credentials. The repository contains no shared keys. Subscription and institutional entitlements can affect access.

## Offer setup once

If any key is missing, name the missing sources and ask one concise question, adapted to the observed status:

> Article search can use Scopus, Semantic Scholar, and Web of Science Starter. [Missing sources] are not configured. Would you like setup instructions, or shall I continue with the available sources? Please enter keys only in your local environment settings, not in this chat.

Use a nonblocking question when the host supports it and continue independent work. If none is configured, offer public web search or user-provided articles as alternatives. If the user specifically requires a missing database, explain the limitation and wait for setup or an alternate-source choice before claiming to search it. Do not require all three keys. If all are configured, proceed without a setup question.

Honor a user's decision to skip setup for the rest of the conversation. Do not repeat the prompt on every query. A fresh conversation may check again; do not claim permanent first-run memory or save secret-bearing setup state. If setup changes, recheck availability privately. Authentication failures should prompt a short source-specific correction, not repeated requests for keys.

## Private configuration guidance

On Windows, open **Edit environment variables for your account**, add the chosen variable and paste the key in its value field. Reopen the agent application so new processes inherit it. Do not ask users to paste keys into chat or commands that are recorded in shell history.

On macOS/Linux or managed hosts, use the launcher's private environment/secret settings to inject the selected variable into the agent process. For terminal launches, a masked local prompt (for example Python `getpass`) can read a key and pass it in the child process environment without placing it in command history. Explain that such a child-process setting lasts only for that launch. Use host-specific configuration instructions when persistence is needed; do not put credentials into the skill bundle or a tracked shell/configuration file.

After configuration, report availability only. Use the user's next requested search to verify access, and distinguish missing credentials, rejected credentials, insufficient entitlements, and quota limits. Never echo request headers or unredacted server error bodies containing credentials.
