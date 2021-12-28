import instaloader

test = instaloader.Instaloader() 
acc = input("Enter username: ") 
test.download_profile(acc, profile_pic_only=True)
