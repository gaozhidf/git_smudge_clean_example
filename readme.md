# git smudge and clean example

## Description
git filter example cleaning sensitive keywords from specific json files

## Info
git filter details, see https://git-scm.com/book/en/v2/Customizing-Git-Git-Attributes
![git filter smudge](https://git-scm.com/book/en/v2/images/smudge.png)
![git filte clean](https://git-scm.com/book/en/v2/images/clean.png)

## Setup Steps:

#### Add `Git Attributes`
Add `.gitattributes` in your workspace, and add content as below
```
echo 'configData.json    filter=keyfilter' >> .gitattributes
```

Or edit `.git/info/attributes` if you don’t want the attributes file committed with your project
```
echo 'configData.json    filter=keyfilter' >> .git/info/attributes
```

#### Add `Git Config Filter`
1. Copy `keyfilter.py` or `keyfilter.js` into your project
2. To avoid `keyfilter.py` or `keyfilter.js` to be commited, add it into `.gitignore` or `.git/info/exclude`

3. Add filter to config. These will add to `.git/config`, which will not be committed with your project
```
git config filter.keyfilter.smudge "./keyfilter.py smudge"
git config filter.keyfilter.clean "./keyfilter.py clean"
```

or

```
git config filter.keyfilter.smudge "./keyfilter.js smudge"
git config filter.keyfilter.clean "./keyfilter.js clean"
```

Alternatively you can add `.gitconfig` as local, which will be committed with your project.
```
git config --local include.path ../.gitconfig
git config --file .gitconfig filter.keyfilter.smudge "./keyfilter.py smudge"
git config --file .gitconfig filter.keyfilter.clean "./keyfilter.py clean"
```

or use node script

The result is this content added to selected file:
```
[filter "keyfilter"]
        smudge = keyfilter.py smudge
        clean = keyfilter.py -clean
```

## Note:
Avoid to use simple keywords, which may conflict with replace content, for example:
```
{
    "username": "user"
    "password": "pass"
}
```
