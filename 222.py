class Movie:
    def __init__(self, title, director, year, genre="Unknown"):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
        self.rating = None  # 初始化评分为空

    def info(self):
        """返回电影的完整信息"""
        return f"{self.title} ({self.year}), directed by {self.director}, Genre: {self.genre}, Rating: {self.rating or 'N/A'}"

    def set_rating(self, rating):
        """给电影评分"""
        if 0 <= rating <= 10:
            self.rating = rating
        else:
            print("Rating must be between 0 and 10")


# 模拟电影收藏
if __name__ == "__main__":
    # 创建多个电影对象
    m1 = Movie("Inception", "Nolan", 2010, "Sci-Fi")
    m2 = Movie("The Matrix", "Wachowski", 1999, "Action")
    m3 = Movie("Interstellar", "Nolan", 2014, "Sci-Fi")

    # 设置评分
    m1.set_rating(9)
    m2.set_rating(8.5)

    # 打印电影信息
    for movie in [m1, m2, m3]:
        print(movie.info())
