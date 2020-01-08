'''
Select random lines out of a text file and save to another file.
'''

import argparse
import os
import random
import itertools
import time

import googlesearch

PAPER_DOMAINS = ['arxiv.org', 'openaccess.thecvf.com', 'www.semanticscholar.org']
CODE_DOMAINS = ['github.com', 'bitbucket.org', 'gitlab.com']


def title_to_paper_link(title):
    try:
        paper_gen = googlesearch.search(title, num=10, stop=1, domains=PAPER_DOMAINS, user_agent=googlesearch.get_random_user_agent())
        paper_link = next(itertools.islice(paper_gen, 0, None))
    except:
        paper_gen = googlesearch.search(title, num=10, stop=1, user_agent=googlesearch.get_random_user_agent())
        paper_link = next(itertools.islice(paper_gen, 0, None))
    return paper_link


def title_to_code(title):
    try:
        code_gen = googlesearch.search(title + 'github', num=10, stop=1, domains=CODE_DOMAINS, user_agent=googlesearch.get_random_user_agent())
        code_link = next(itertools.islice(code_gen, 0, None))
    except:
        code_gen = googlesearch.search(title + 'github', num=10, stop=1, user_agent=googlesearch.get_random_user_agent())
        code_link = next(itertools.islice(code_gen, 0, None))
    return code_link


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--title', required=True, type=str, help='the title of the paper')

    opt = parser.parse_args()

    paper_link = title_to_paper_link(opt.title)
    code_link = title_to_code(opt.title)
    print('Paper: {0}'.format(paper_link))
    print('Code: {0}'.format(code_link))


if __name__ == "__main__":
    main()
