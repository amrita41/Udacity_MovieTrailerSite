import fresh_tomatoes
import media
def main():

    bh = media.Movie("Bharat",
                          "Journey of a man and nation together!",
                          "https://i0.wp.com/bollymoviez.com/wp-content/uploads/2019/03/Bharat-Movie-Release-Date-Cast-Poster-Bharat-Trailer-2.jpg?w=597",
                          "https://www.youtube.com/watch?v=Ea_GKoe81GY",
                          "June 5, 2019")

    ae = media.Movie("Avengers: EndGame",
                          "The Avengers take a final stand against Thanos",
                          "https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_.jpg",
                          "https://www.youtube.com/watch?v=TcMBFSGVi1c",
                          "April 26, 2019")

    ach = media.Movie("Annabelle Comes Home",
                          "Determined to keep Annabelle from wreaking more havoc",
                          "https://m.media-amazon.com/images/M/MV5BYmI4NDNiMmQtZTFkYi00ZDVmLThlYTAtMWJlMjU1M2I2ZmViXkEyXkFqcGdeQXVyNjg2NjQwMDQ@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                          "https://www.youtube.com/watch?v=EMa-KFfatT0",
                          "June 26, 2019")

    kb = media.Movie("Kabir Singh",
                          "A short-tempered house surgeon plays a romantic drama",
                          "https://pbs.twimg.com/profile_images/1055678140901539841/UujHGuWZ_400x400.jpg",
                          "https://www.youtube.com/watch?v=RiANSSgCuJk",
                          "June 21, 2019")

    xm = media.Movie("X-Men: Dark Phoenix",
                          "Jean Grey begins to develop incredible powers",
                          "https://m.media-amazon.com/images/M/MV5BMjAwNDgxNTI0M15BMl5BanBnXkFtZTgwNTY4MDI1NzM@._V1_.jpg",
                          "https://www.youtube.com/watch?v=azvR__GRQic",
                          "June 7, 2019")
                    
    spr = media.Movie("Super 30",
                          "Life of a Mathematician, Anand Kumar and his educational program-Super 30",
                          "https://upload.wikimedia.org/wikipedia/en/2/29/Super_30_The_Film.jpg",
                          "https://www.youtube.com/watch?v=QpvEWVVnICE",
                          "July 12, 2019")

    sm = media.Movie("Spider-Man: FFH",
                          "Following the events of Avengers: Endgame,",
                          "https://terrigen-cdn-dev.marvel.com/content/prod/1x/sffh_venice-high-res.jpg",
                          "https://www.youtube.com/watch?v=Nt9L1jCKGnE",
                          "July 5, 2019")

    lk = media.Movie("The Lion King",
                          "The story of Simba, a young lion!!",
                          "http://images6.fanpop.com/image/photos/42700000/Poster-the-lion-king-2019-42737783-555-822.jpg",
                          "https://www.youtube.com/watch?v=7TavVZMewpY",
                          "July 19, 2019")

    sz = media.Movie("Shazam!",
                          "An effortlessly entertaining blend of humor and heart",
                          "https://m.media-amazon.com/images/M/MV5BYTE0Yjc1NzUtMjFjMC00Y2I3LTg3NGYtNGRlMGJhYThjMTJmXkEyXkFqcGdeQXVyNTI4MzE4MDU@._V1_.jpg",
                          "https://www.youtube.com/watch?v=uilJZZ_iVwY",
                          "April 5, 2019")

    movies = [bh, ae, ach, kb, xm, spr, sm, lk, sz]

    fresh_tomatoes.open_movies_page(movies)

main()
