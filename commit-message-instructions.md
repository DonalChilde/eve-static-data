# Commit Message Conventions

## Subject line

- Write in the imperative mood: "Add", "Fix", "Update" — not "Added", "Fixes", "Updated".
- Keep it to 50 characters or fewer.
- No trailing period.
- Summarize *what* changed, not how.

## Body

- Leave a blank line after the subject.
- Wrap body lines at 72 characters.
- Required for any non-trivial change. Explain *why* the change was made, not
  just what — the diff already shows what changed.
- use a blank line between explainations of changes.
- Optional for trivial changes (typo fixes, formatting-only, small doc tweaks),
  where a subject line alone is enough.
- Do not include issue numbers in the commit body. Issue references (e.g.
  `Closes #58`) belong on the pull request, not on individual commits.
- Do not include judgements like "improves maintainability" or "improves user guidance"

## Style

- No type prefixes (no `feat:`, `fix:`, `chore:`).
- No emoji/gitmoji.
- Never write vague messages like "wip", "fix stuff", or "updates".

## Example

Good:

```
Fix off-by-one error in blueprint report pagination

The last page of results was being dropped because the offset
calculation didn't account for the final partial page.
```

Bad:

```
fix: wip updates
```
