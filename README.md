# jaat-api

[![PyPI version](https://img.shields.io/pypi/v/jaat-api.svg)](https://pypi.org/project/jaat-api/)
[![License](https://img.shields.io/github/license/sjmeis/jaat-api.svg)](https://github.com/sjmeis/jaat-api/blob/main/LICENSE)

The official, lightweight Python client library for the **JAAT** suite of tools. 

`jaat-api` is an easy-to-use, intuitive, session-managed SDK for programtically accessing the open-source JAAT modules. Securely send text batches to the openly hosted JAAT modules.

---

## Installation

Install directly from PyPI:

```bash
pip install jaat-api
```

## Quick Start

Initialize the `JAATClient` with your API key (provided by us) and execute JAAT on your batch texts seamlessly:

```python
from jaat_api import JAATClient

client = JAATClient(api_key="jaat_app_private_key_here")

job_ads = [
    "[JOB AD TEXT 1]",
    "[JOB AD TEXT 2]",
    "..."
]

task_results = client.run_batch("task", job_ads) # alternatively, client.get_tasks(job_ads)

# continue to run other jobs
skill_results = client.run_batch("skill", job_ads)
```

## Helpful Tips

### Handling Exceptions

The SDK provides a structured `JAATError` instance whenever an operation breaks down or fails. Ideally, wrap jobs within try/except blocks to handle these conditions gracefully:

```python
from jaat_api import JAATError

try:
    ## as before
except JAATError as e:
    print(f"Extraction failed (Status Code: {e.status_code})")
    print(f"Error Context: {e.message}")
```

### Sandbox Public Evaluation
Anyone looking to evaluate the platform programmatically before contacting us for a dedicated token can use the public sandbox key:

```python
client = JAATClient(api_key="jaat_public_sandbox_testing_key")

try:
    results = client.get_tasks(["JOB AD TEXT"])
    print(results)
except JAATError as e:
    if e.status_code == 429:
        print("Sandbox daily evaluation volume exhausted. Please rotate to a private key.")
```

As can be seen, the public API key is highly throttled and is strictly for testing purposes. The current usage of this key is limited to one request per day, per IP.

### License
`jaat-api` (and `JAAT`) are distributed under the MIT License. See `LICENSE` for more information.

## Getting a Key

We will soon be releasing a contact form to let us know your interest in receiving a private API key. Stay tuned!

## Citation
This code and the overarching `JAAT` package is part of ongoing work to leverage lightweight, but powerful NLP tools to unlock structured, coded data from job posting data.

If you find this software useful, please consider citing:

```
@article{meisenbacher2025extracting,
  title={Extracting O* NET Features from the NLx Corpus to Build Public Use Aggregate Labor Market Data},
  author={Meisenbacher, Stephen and Nestorov, Svetlozar and Norlander, Peter},
  journal={arXiv preprint arXiv:2510.01470},
  year={2025}
}
```