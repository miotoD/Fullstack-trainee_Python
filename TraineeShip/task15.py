#blog app

import os

def blog():
    
    blogFile = "C:\\Users\\asus\\Desktop\\blog.txt"
    print("----------------Welcome to the Python Blog App.---------------")
    print("1 Create Blog")
    print("2 View Blogs")
    print("3 Edit Blog")
    print("4 Delete Blog")

    
    # function to add the blog in the text file
    def addBlog():
        print("Enter the blog title:",end="")
        title = input("").strip()
        
        print("Enter the content for the blog:",end="")
        content = input().strip()
        
        
        
        with open(blogFile,"a+") as file:
            
            file.seek(0, os.SEEK_END)
            
            if file.tell()>0:
                file.write("\n")
            
            file.write(title)
            file.write(" : ")
            file.write(content)
            
            print("Blog Succesfully Created!")
            print("----------------------------------------")
            
    
       #function to view the blogs from the text file
             
    def viewBlog():
     print("--Dipslaying Blogs--")
     with open(blogFile, "r") as file:
         data = file.read()
         print(data)        
    
    
     #function to edit blog
    def editBlog():
        
        contentUpdates = []
        print("Enter blog title to edit:",end="")
        title = input()
        
        blogFound = False
        
        with open(blogFile,"r") as file:
            contents = file.read().split("\n")
            
            for blogs in contents:
                
                if title in blogs:
                    contentUpdates = blogs.split(":")                    
                #     #logic to update the content
                    print("Update the content:",end="")
                    updatedContent = input().strip()
                    contentUpdates.pop(1)
                    contentUpdates.insert(1,updatedContent)     
                    
                    #logic to add the updated content to list again
                    contents[contents.index(blogs)] = ":".join(contentUpdates)
                    
                    
                    blogFound = True  
                    break
                else:
                    contentUpdates.append(f"{blogs} \n")
                
            print(contents)
            
            if not blogFound:
                print("No such blog exists")
            
            if blogFound:
                with open(blogFile, "w") as file:
                    file.write("\n".join(contents))  
                    print("Blog updated successfully!")
                    
    def deleteBlog():
        print("Enter the title of the blog to delete:",end="")
        dltInput = input()
        
        blogFound = False
        afterDeletion = []
                
        with open(blogFile, "r+") as file:
            for lines in file:             
                if(dltInput in lines):
                    continue
                else:
                    afterDeletion.append(lines)       
        
        with open(blogFile,"w") as file:
            file.writelines(afterDeletion)
        
        
        
        
        
    
    while True:
        print("--------------------")
        print("Enter 5 to Exit")
        userInput = input()
        
        if(userInput == "1"):
            addBlog()
        
        if(userInput == "2"):
            viewBlog()
        
        if(userInput == "3"):
            editBlog()
        
        if(userInput == "4"):
            deleteBlog()
            
                
        if(userInput == "5"):
            break
        
    
    
blog()