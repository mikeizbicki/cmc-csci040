#!/bin/sh

urls='
https://tsl.news/
https://www.claremontindependent.com/
https://www.cmcforum.com/
https://www.scrippscollege.edu/news/tag/artificial-intelligence
https://www.pomona.edu/news
https://www.hmc.edu/about/news/
https://www.kgi.edu/about/branding-news-pr/news/
https://www.cmc.edu/newsfeed
https://www.pitzer.edu/news
https://www.cgu.edu/news/
'

for url in $urls; do
    echo url
    python3 ragnews.py --add_url="$url" --recursive_depth=5 --db=claremont.db --loglevel=INFO
done

