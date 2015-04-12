rm data/* -rf
rm worker.log
rm master.log
find . -name '*.pyc' | xargs -i -t rm {}
