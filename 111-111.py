import requests
import pandas as pd
import time


def fetch_mcmaster_news(per_page=20, max_pages=5, output_csv="mcmaster_news.csv"):
    """
    抓取 McMaster News 网站新闻（WordPress REST API）

    参数：
        per_page: 每页抓取数量 (最大 100)
        max_pages: 最大抓取页数
        output_csv: 保存 CSV 文件名
    """
    base_url = "https://news.mcmaster.ca/wp-json/wp/v2/posts"
    all_posts = []

    for page in range(1, max_pages + 1):
        params = {
            "per_page": per_page,
            "page": page
        }
        try:
            resp = requests.get(base_url, params=params, timeout=10)
            resp.raise_for_status()
            posts = resp.json()
            if not posts:
                break  # 没有更多新闻，结束抓取
            for post in posts:
                all_posts.append({
                    "title": post["title"]["rendered"],
                    "link": post["link"],
                    "date": post["date"],
                    "excerpt": post["excerpt"]["rendered"]
                })
            print(f"第 {page} 页抓取完成，已累计 {len(all_posts)} 条新闻")
            time.sleep(1)  # 控制抓取频率，避免请求过快
        except requests.RequestException as e:
            print(f"第 {page} 页请求失败: {e}")
            break

    # 转为 DataFrame 并保存 CSV
    df = pd.DataFrame(all_posts)
    df.to_csv(output_csv, index=False, encoding="utf-8")
    print(f"\n总共抓取 {len(df)} 条新闻，已保存到 {output_csv}")
    return df


# ------------------ 测试 ------------------
if __name__ == "__main__":
    df_news = fetch_mcmaster_news(per_page=20, max_pages=5)
    print(df_news.head())
