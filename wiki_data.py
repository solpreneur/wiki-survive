"""Wikipedia article-retrieval skeleton for Wiki Survival."""

import wikipediaapi
import random

Article = dict[str, str]


def get_wikipedia_articles(
    topic: str,
    search_count: int = 7,
    required_count: int = 5,
) -> list[Article]:
    """Return five usable article titles and one-sentence summaries.

    Search seven Wikipedia articles so that two can be used as backups when
    an article is missing, ambiguous, or otherwise unusable.
    """

    client = get_wiki_client()
    try:
        page = get_wiki_page(topic, client)
    except ValueError as error:
        print(f"ERROR: {error}")
    else:
        articles = []

        while len(articles) < required_count:
            articles_from_page = get_articles_from_page(page, search_count)
            articles = get_articles(articles_from_page, required_count)

        return articles


def get_wiki_client():
    return wikipediaapi.Wikipedia(user_agent="wiki-survive", language="en")


def get_wiki_page(page_name, client):
    """Gets the page name and the wiki-client and
    returns the page in case that there is no exception and the page exists
    """
    page = client.page(page_name)

    if not page.exists():
        raise ValueError(f"Wikipedia has no page for the topic {page_name}")
    else:
        return page


def get_articles_from_page(page, search_count):
    """Gets a list of random articles linked in the given page until a given
    number of articles is reached
    """
    possible_articles = []
    link_titles = list(page.links.keys())

    while len(possible_articles) < search_count:
        random_index = random.randrange(0, len(link_titles))
        random_link_title = link_titles[random_index]
        random_article = page.links[random_link_title]
        if random_article.namespace == wikipediaapi.Namespace.MAIN:
            possible_articles.append(
                {"title": random_link_title, "page": random_article}
            )

    return possible_articles


def get_articles(article_list, required_count):
    """Choosing a given number of articles which exist from the given article
    list
    """
    articles = []

    for article in article_list:
        if article["page"].exists():
            first_sentence = article["page"].summary.split(".")[0]
            articles.append(
                {
                    "title": article["title"],
                    "summary": first_sentence,
                }
            )
        if len(articles) == required_count:
            break

    return articles


if __name__ == "__main__":
    print(get_wikipedia_articles("List_of_fish_by_common_name"))
    print("------------------")
    print(get_wikipedia_articles("List_of_English_people"))
    print("------------------")
    print(get_wikipedia_articles("List_of_dinosaur_genera"))
