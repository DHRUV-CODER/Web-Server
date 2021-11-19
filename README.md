
# About 

This is a simple Web Server to view/share your file on your local network.
You can potentially use this to open a file/folder on your other device without worrying about sending/downloading on the device.

Using this you can save time and all the hassle of sharing is gone.

# Steps to Download


Download the latest exe from [Here](https://github.com/DHRUV-CODER/Web-Server/releases/tag/exe)

![image](https://user-images.githubusercontent.com/60794694/142603655-7fea010b-c8dc-4ca4-9b51-d02e12fea577.png)

Then put in the **Directory** that you want to share.

Example : Desktop 

![image](https://user-images.githubusercontent.com/60794694/142603997-a5e8f717-4b2e-4951-8a8c-a3f3b2fb3077.png)

Open the **exe** and wait till it is Hosted on port **5000** 

![image](https://user-images.githubusercontent.com/60794694/142604224-0dfd596b-812d-4fb6-a433-a6a78fe1ac98.png)

After that , open your preferred Browser and go to [127.0.0.1:5000](http://127.0.0.1:5000/) or [localhost:5000](http://localhost:5000/)

There you can see all the files and folders 

![image](https://user-images.githubusercontent.com/60794694/142604591-6db3a7e9-e6a8-49a8-bd1d-79137f7e275c.png)

You can click on respective folders and view the content

![image](https://user-images.githubusercontent.com/60794694/142604961-a3df5129-2a64-47a8-ab64-9d01f0a3a002.png)

We also support syntax highlighting which makes the content inside more readable, *syntax highlighting is available for almost every type of file extension* 

![image](https://user-images.githubusercontent.com/60794694/142605205-59267dec-71b2-4889-a688-47d46201c5b6.png)

There are some file which cant be previewed , instead you can download it  and use.

![image](https://user-images.githubusercontent.com/60794694/142605386-1d9e09a7-027d-4e2c-9af4-1679ed43430c.png)

<img width="957" alt="image" src="https://user-images.githubusercontent.com/60794694/142605557-1fac2a86-c922-4e7d-9ec0-827e65aa6866.png">


Well these were some of the features .

# Below feature is yet to be implemented
# I want to share it on my local network , how do i visit on other device ?

![image](https://user-images.githubusercontent.com/60794694/142610960-3b1377b8-4be5-4600-addd-acb62a0c5701.png)

**Click allow**

And that is your url , now you can use this url to visit on other device

# or , if you can't find the url

Well it is pretty simple , Find you hosted device's physical address  and put `:5000` behind it .

**For Eg:**

You can open `cmd` or `powershell` upto you, and type `ipconfig` there you can find your hosted device's physical address.
 

<img width="595" alt="image" src="https://user-images.githubusercontent.com/60794694/142606159-ddc9aaa8-733c-46f0-9c04-0bea6f8b7dd8.png">

 In my case it is `192.168.100.3` , so to visit the webserver put  port `:5000` behind it . Final uri `192.168.100.3:5000`
# I want to share it publicly to my friends and colleagues ? How do i ?

One way can be port forwarding and stuff . Which is pretty boring and complex.

Instead i suggest you to use a tool like [ngrok](https://ngrok.com/)

**What is the use Ngrok?**

ngrok  **allows you to expose a web server running on your local machine to the internet**. Just tell ngrok what port your web server is listening on.

[Download ngrok](https://ngrok.com/download)

After Downloading , open the folder which it is in using your preferred terminal.  

In my case i pasted it in Desktop 

![image](https://user-images.githubusercontent.com/60794694/142607864-633fa941-e7df-40c6-8275-1161b2dd90fc.png)

Then type this command to run **ngrok** on port **5000**

This will expose the port `5000` to the internet

![image](https://user-images.githubusercontent.com/60794694/142608254-0e3b0132-a295-49d4-b1d4-dc6c9ed19343.png)

and hit **Enter**

![image](https://user-images.githubusercontent.com/60794694/142608366-2ffbb5a8-18e8-46ae-bb5d-c946fa56323a.png)

Command: `./ngrok http 5000`

Copy the url  provided by ngrok , now you can share / view it publicly.

**Note**: As i am using the free version it , this stay online for temporary time period only. I mean 5-6 hrs enough ig , You can always rerun it for new url .

To close it , simply press `ctrl+c`

# Bonus
There is a inbuilt cli command , which will provide you with web server, it is uglier and not that useful .

Commands : `python3 -m http.server 5000`

You just need python for this. 

# Conclusion

Well that it for the steps . If you find any typos , feel free to send a pull request.

Hope it helps you. 
