To reproduce the extraction-running-time evaluation, do the following:

- Install the requierements in a virtualenv:

        sudo pip install virtualenv; virtualenv ENV; source ENV/bin/activate
        sudo pip install lxml, feedparser, goose-extractor, python-readability, boilerpipe

- Get the version of the BlogForever Crawler used for the evaluation:

        git clone git@github.com:BlogForever/crawler.git
        git checkout 06a1fd89554db518c6348aba3c1709d85cce2c42

- Merge it with running-times/crawler:

        rsync -aplx --link-dest=crawler/ blogforever-crawler-publication/running-times/crawler/ merged/

- Run the evaluation:

        sudo python -m bibcrawl/run
