#https://classroom.udacity.com/courses/ud036
import media
import fresh_tomatoes

fast_and_furious = media.Movie("Fast and Furious 1",
                        "Los Angeles police officer Brian O'Conner must decide where his loyalty really lies when he becomes enamored with the street racing world he has been sent undercover to destroy.",
                        "https://upload.wikimedia.org/wikipedia/th/2/28/The_Fast_and_the_Furious_poster.jpg",
                        "https://youtu.be/2TAOizOnNPo")

#print(fast_and_furious.storyline)

avengers = media.Movie("The Avengers",
                     "Earth's mightiest heroes must come together and learn to fight as a team if they are going to stop the mischievous Loki and his alien army from enslaving humanity.",
                     "https://upload.wikimedia.org/wikipedia/en/8/8a/The_Avengers_%282012_film%29_poster.jpg",
                     "https://youtu.be/eOrNdBpGMv8")

# print(avengers.storyline)
# avengers.show_trailer()

star_wars = media.Movie("Star Wars: Episode III", 
                        "Jedi hero Anakin Skywalker is seduced by the dark side of the Force to become the Emperor's new apprentice -- Darth Vader.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/9/93/Star_Wars_Episode_III_Revenge_of_the_Sith_poster.jpg/220px-Star_Wars_Episode_III_Revenge_of_the_Sith_poster.jpg",
                        "https://youtu.be/5UnjrG_N8hU")

harry_potter = media.Movie("Harry potter 1",
                          "An orphaned boy enrolls in a school of wizardry, where he learns the truth about himself, his family and the terrible evil that haunts the magical world.",
                          "https://i.pinimg.com/originals/57/40/7a/57407a21c0d0e216bf270d8b219a79ce.jpg",
                          "https://youtu.be/VyHV0BRtdxo")

iron_man = media.Movie("Iron Man 1",
                        "Tony Stark creates a unique weaponized suit of armor to fight evil.",
                        "https://upload.wikimedia.org/wikipedia/th/2/20/Ironmanposter.jpg",
                        "https://youtu.be/8ugaeA-nMTc")

pirates_of_the_caribbean = media.Movie("Pirates of the Caribbean: The Curse of the Black Pearl",
                           "Captain Jack Sparrow to save his love, the governor's daughter, from Jack's former pirate allies, who are now undead.",
                           "https://upload.wikimedia.org/wikipedia/th/0/0e/Pirates_of_the_Caribbean_movie.jpg",
                           "https://youtu.be/naQr0uTrH_s")   

movies = [fast_and_furious, avengers, star_wars, harry_potter, iron_man, pirates_of_the_caribbean]
fresh_tomatoes.open_movies_page(movies)
