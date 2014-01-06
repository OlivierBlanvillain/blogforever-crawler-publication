To reproduce the success-rates evaluation, do the following:

- Generate the test-set as explained in `/dataset`.
- Install the requierements in a virtualenv:

        sudo pip install virtualenv; virtualenv ENV; source ENV/bin/activate
        sudo pip install lxml, feedparser, goose-extractor, readability-lxml, boilerpipe

- Get the version of the BlogForever Crawler used for the evaluation:

        git clone git@github.com:BlogForever/crawler.git
        git checkout 06a1fd89554db518c6348aba3c1709d85cce2c42

- Merge it with success-rates/crawler:

        mkdir merged; sudo cp -al crawler/* blogforever-crawler-publication/success-rates/crawler/* merged/

- Run all the extractions:

        # for * in success-rates/title/, * in success-rates/article/, and crawler/
        (cd path/to/project; sudo python gen.sh)

- Compute the scores:

        success-rates/scroeAll.sh
        success-rates/scroeTitles.sh
