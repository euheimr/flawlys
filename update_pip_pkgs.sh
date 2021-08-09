pip3 list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U
pip3 freeze > requirements.txt

find requirements.txt -type f -exec sed -i "" "s/==/>=/g" {} \;

# Do a package upgrade
pip install -r requirements.txt --upgrade
