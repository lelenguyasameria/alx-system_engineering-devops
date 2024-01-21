# Apache 500 Error Fix

This project contains Puppet manifests to identify and fix a 500 error in Apache using strace.

## Usage

1. Attach strace to Apache process using tmux.
2. Run curl in another tmux window to trigger the error.
3. Analyze strace output to identify the issue.
4. Manually fix the issue.
5. Use Puppet to automate the fix.

## Puppet Manifests

- `0-strace_is_your_friend.pp`: Puppet code to fix the identified Apache issue.

## Running Puppet

Ensure you are using Puppet v3.4. Run the following command:

```bash
$ puppet apply 0-strace_is_your_friend.pp

