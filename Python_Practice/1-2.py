posts = int(input("게시글의 총 개수를 입력하세요 "))
posts_per_page = int(input("한 페이지에 필요한 게시글 수를 입력하세요 "))

total_pages = posts // posts_per_page

print(total_pages)
