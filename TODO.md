#TODO

- Edit button in resource list to come only to the creator.
- when vote is done, redirect to previous page.
- Raise 404 if user is inactive.
- Add proper regex to match recent and popular tabs in resources.
- Use select_related and prefetch_related tag wherever possible to reduce number of database queries. But use them with caution *READ django1.4docPDF page827 last para*.
- Make users in advance with usernames projects, feeds, tracks, blog, codesters, admin.
- Add something to do the numbering/sequencing of chapters in tracks.
- Add feed list view from a domain with domain template tag filter.

#DONE

- Make heading template context variable and remove whole page_title if not used.
- Figure out how to record a person's vote
- Filter Snippets and resource when show is True.
- reduce main navbar height a bit by changing logo icon to 18px.
- Limit explore boxes to show only 6 items.
- Remove all unnecessary import from all files.
- While saving any object, make sure to assign permission to the creator and others
- *IMPORTANT* student-profile url is using student pk but in blog base template, it is given user pk. It can lead to problems amend it.
- Make blog edit views.
- Change Post app name to Feed and Post model to Feed everywhere
