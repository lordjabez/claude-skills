# README Examples

Both are invented tools written to match the observed patterns. Real READMEs
are in his public GitHub repos.

## Backup Rotator (script)

````markdown
# Backup Rotator

This repository contains a Bash script that prunes old S3 backup objects while
keeping one per week for the last six months. It currently only handles keys named
with an ISO date prefix.

It's used to keep the bill down for my home NAS backups.


## Prerequisites

- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)
- [jq](https://jqlang.github.io/jq/download/)

The script assumes the AWS CLI is already configured for the account that owns the bucket.


## Usage

Run the script with the bucket name and an optional prefix:

```bash
./rotate-backups.bash BUCKET [PREFIX]
```

- `BUCKET` is the name of the bucket, without the `s3://` scheme
- `PREFIX` limits the scan to keys under that folder (e.g. `nas/`)

Add `--dry-run` as the last parameter to list what would be deleted without deleting it.
Note that versioned buckets will keep delete markers, so empty those separately.


## To-Do

- Make the retention window configurable, vs being hard-coded to six months
- Figure out what to do about keys that don't start with a date


## References

- [S3 Lifecycle Configuration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
````

## Env File Loader (published package)

````markdown
# Env File Loader

[![Tests](https://github.com/example/env-file-loader/actions/workflows/test.yml/badge.svg)](https://github.com/example/env-file-loader/actions/workflows/test.yml)
[![Linter](https://github.com/example/env-file-loader/actions/workflows/lint.yml/badge.svg)](https://github.com/example/env-file-loader/actions/workflows/lint.yml)

This Python package makes it easy to load environment variables from an AWS Secrets
Manager secret instead of a `.env` file, so credentials never have to sit on disk.
It currently only supports secrets stored as flat JSON objects.


## Prerequisites

Installation is via `pip`:

```bash
pip install env-file-loader
```

The caller needs `secretsmanager:GetSecretValue` on the secret, via whatever credentials
the [default boto3 chain](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html)
finds.


## Usage

Basic usage is as follows:

```python
import env_file_loader

# Reads the secret and copies each key into os.environ
env_file_loader.load('my-app/config')

# Same, but skips keys that are already set in the environment
env_file_loader.load('my-app/config', override=False)
```

The secret name can be a full ARN if the secret lives in another account. Values that are
not strings are converted with `str()`, which is probably not what you want for nested
objects.

In a more complex example, two secrets are merged with the second taking precedence
(this was the original reason for building the library, since staging and production
share most of their settings).

```python
env_file_loader.load('my-app/common')
env_file_loader.load('my-app/staging')
```


## To-Do

- Support nested JSON by flattening keys with underscores
- Add caching, since right now every call hits the API
````
