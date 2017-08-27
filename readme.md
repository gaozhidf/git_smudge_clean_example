
# git smudge and clean example
> Help you avoid to commit your sensitive keywords

git filter details, see https://git-scm.com/book/en/v2/Customizing-Git-Git-Attributes
![git filter smudge](https://git-scm.com/book/en/v2/images/smudge.png)
![git filte clean](https://git-scm.com/book/en/v2/images/clean.png)

## Setup Steps:

#### Add `keyfilter.py`
1. copy `keyfilter.py` into your project
2. to avoid committed `keyfilter.py`, add it into `.gitignore`

#### Add `Git Attributes`

1. Add `.gitattributes` in your workspace, and add content as below
```
configData.json    filter=keyfilter
```
2. Or edit `.git/info/attributes` if you don’t want the attributes file committed with your project
```
echo 'configData.json    filter=keyfilter' >> .git/info/attributes
```

#### Add `Git Config Filter`
1. Add by command and it will add in `.git/config`, which will not be committed with your project
```
git config filter.keyfilter.smudge "python keyfilter.py --smudge"
git config filter.keyfilter.clean "python keyfilter.py --clean"
```
2. Or edit `.git/config`, which will not be committed with your project
```
[filter "keyfilter"]
        smudge = python keyfilter.py --smudge
        clean = python keyfilter.py --clean
```
3. Or add `.gitconfig` as local, which will be committed with your project. and add content in last step
```
git config --local include.path ../.gitconfig
```

## Note:
1. Avoid to use simple keywords, which may conflict with replace content, for example:
```
{
    "username": "user"
    "password": "pass"
}
```
