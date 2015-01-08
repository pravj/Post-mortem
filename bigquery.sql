SELECT repository_url, MAX(repository_watchers) as stars
FROM [githubarchive:github.timeline]
WHERE
    PARSE_UTC_USEC(created_at) <= PARSE_UTC_USEC("2015-01-08 00:00:00") AND
    repository_watchers >= 500
GROUP EACH BY repository_url
ORDER BY stars DESC
LIMIT 10000
