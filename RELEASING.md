# Release Checklist

* [ ] Get master to the appropriate code release state.
* [ ] Update version in `whatsonthemenu/__init__.py` and `setup.py` and commit:
```bash
git checkout master
edit whatsonthemenu/__init__.py setup.py
git add whatsonthemenu/__init__.py setup.py
git commit -m "Release 0.1.0"
```
* [ ] Tag the last commit with the version number:
```bash
git tag -a 0.1.0 -m "Release 0.1.0"
```
* [ ] Release on PyPI:
```bash
python setup.py register
python setup.py sdist --format=gztar upload
```
* [ ] Check installation: `pip install -U whatsonthemenu`
* [ ] Push: `git push`
* [ ] Push tags: `git push --tags`
* [ ] Create new GitHub release: https://github.com/hugovk/whatsonthemenu/releases/new
  * Tag: Pick existing tag "0.1.0"
  * Title: "Release 0.1.0"
```
