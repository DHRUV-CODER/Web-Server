# Topics Covered

> **`Click and go`**

- [About](https://github.com/DHRUV-CODER/Web-Server#about)
- [Security Risks](https://github.com/DHRUV-CODER/Web-Server#security-risks-)
- [Running using python](https://github.com/DHRUV-CODER/Web-Server#run-using-python)
- [Steps to download exe](https://github.com/DHRUV-CODER/Web-Server#steps-to-download-the-exe)
- [Using exe if python is not installed](https://github.com/DHRUV-CODER/Web-Server#steps-to-download-the-exe)
- [Accessing on local network](https://github.com/DHRUV-CODER/Web-Server#i-want-to-share-it-on-my-local-network--how-do-i-visit-on-other-device-)
- [Finding Hosted Device's physical address](https://github.com/DHRUV-CODER/Web-Server#or--if-you-cant-find-the-url)
- [Making it publicly available](https://github.com/DHRUV-CODER/Web-Server#i-want-to-share-it-publicly-to-my-friends-and-colleagues--how-do-i-)
- [Bonus](https://github.com/DHRUV-CODER/Web-Server#bonus)
- [Credits](https://github.com/DHRUV-CODER/Web-Server#credits)

# About 

> This is a simple Web Server to view/share your file on your local network.
> You can potentially use this to open a file/folder on your other device without worrying about sending/downloading on the device.

> Using this you can save time and all the hassle of sharing is gone.

![ezgif-2-7a1f23866be4](https://user-images.githubusercontent.com/60794694/142751034-82d52634-4773-4f4d-a0f7-fc46b1ca90bf.gif)

# Security Risks ?
> Don't Run this on a public wifi ie:(starbucks,airport wifi etc..), as other can visit and view the content.
> 
> If you want to access only on you hosted device for some reason then remove [`host=0.0.0.0,`](https://github.com/DHRUV-CODER/Web-Server/blob/main/server.py#L29)
> 
> If your running on your personal wifi and only trusted users are connected to your wifi , then no worries . **Hakuna Matata**
> 

# Run using python

> 1) Git clone the [repo](https://github.com/DHRUV-CODER/Web-Server.git) or  [Download the zip](https://github.com/DHRUV-CODER/Web-Server/archive/refs/heads/main.zip)
```
git clone https://github.com/DHRUV-CODER/Web-Server.git
cd .\Web-Server
```
### For Linux (**Requires Python3 to be installed**)
```
pip3 install flask
python3 .\server.py
```
### or on other os
```
pip install flask
py .\server.py
```
> 2) After Running the server.py
>
> 3) Website will be **available** on : **[localhost](http://localhost:5000/)**

# Steps to Download the exe (Only for Windows user)

> **Download the latest exe from [Here](https://github.com/DHRUV-CODER/Web-Server/releases/tag/exe)**

![image](https://user-images.githubusercontent.com/60794694/142603655-7fea010b-c8dc-4ca4-9b51-d02e12fea577.png)

> Then put in the **Directory** that you want to share.

> Example : **Desktop**

![image](https://user-images.githubusercontent.com/60794694/142603997-a5e8f717-4b2e-4951-8a8c-a3f3b2fb3077.png)

> Open the **exe** and wait till it is Hosted on port **5000** 

![image](https://user-images.githubusercontent.com/60794694/142611196-ae0c5b9c-dedf-44f3-82a3-e1fdac4964fc.png)

**Click allow if you want to use it on other device**

![image](https://user-images.githubusercontent.com/60794694/142611295-d4d848db-a83b-4865-92ac-6415db691b8d.png)


> After that , open your preferred Browser and go to [127.0.0.1:5000](http://127.0.0.1:5000/) or [localhost:5000](http://localhost:5000/) , **Only visitable on hosted device**
> 
> There you can see all the files and folders 

![image](https://user-images.githubusercontent.com/60794694/142604591-6db3a7e9-e6a8-49a8-bd1d-79137f7e275c.png)

> You can click on respective folders and view the content

![image](https://user-images.githubusercontent.com/60794694/142604961-a3df5129-2a64-47a8-ab64-9d01f0a3a002.png)

> We also support syntax highlighting which makes the content inside more readable, *syntax highlighting is available for almost every type of file extension* 

![image](https://user-images.githubusercontent.com/60794694/142605205-59267dec-71b2-4889-a688-47d46201c5b6.png)

> Well these were some of the features .

# I want to share it on my local network , how do i visit on other device ?

![image](https://user-images.githubusercontent.com/60794694/142610960-3b1377b8-4be5-4600-addd-acb62a0c5701.png)

> **Click allow**

![image](https://user-images.githubusercontent.com/60794694/142611839-d84f56dc-7a15-47c2-923a-80c2062094ab.png)

> **Note:** For you the url might be different
> And that is your url , now you can use this url to visit on other device

# or , if you can't find the url

> Well it is pretty simple , Find you hosted device's physical address  and put `:5000` behind it .

**For Eg:**

> You can open `cmd` or `powershell` upto you, and type `ipconfig` there you can find your hosted device's physical address.
 

<img width="595" alt="image" src="https://user-images.githubusercontent.com/60794694/142606159-ddc9aaa8-733c-46f0-9c04-0bea6f8b7dd8.png">

> In my case it is `192.168.100.3` , so to visit the webserver put  port `:5000` behind it . Final uri `192.168.100.3:5000`

# I want to share it publicly to my friends and colleagues ? How do i ?

> One way can be port forwarding and stuff . Which is pretty boring and complex.
>
> Instead i suggest you to use a tool like [ngrok](https://ngrok.com/)

**What is the use Ngrok?**

> ngrok  **allows you to expose a web server running on your local machine to the internet**. Just tell ngrok what port your web server is listening on.

**[Download ngrok](https://ngrok.com/download)**

> After Downloading , open the folder which it is in using your preferred terminal.  

> In my case i pasted it in Desktop 

![image](https://user-images.githubusercontent.com/60794694/142607864-633fa941-e7df-40c6-8275-1161b2dd90fc.png)

> Then type this command to run **ngrok** on port **5000**

> This will expose the port `5000` to the internet

![image](https://user-images.githubusercontent.com/60794694/142608254-0e3b0132-a295-49d4-b1d4-dc6c9ed19343.png)

> and hit **Enter**

![image](https://user-images.githubusercontent.com/60794694/142608366-2ffbb5a8-18e8-46ae-bb5d-c946fa56323a.png)

> Command: `./ngrok http 5000`

> Copy the url **provided by ngrok** , now you can share / view it publicly.

> **Note**: As i am using the free version it , this stay online for temporary time period only. I mean 5-6 hrs enough ig , You can always rerun it for new url .

> To close it , simply **press** `ctrl+c`

# Bonus

> There is a inbuilt cli command avail with python , which will provide you with web server, it is bit uglier and not that useful for sharing purposes.
>
> Command : `python3 -m http.server 5000`
>
> You just need python for this. 

# Conclusion

> Well that it for the steps . If you find any typos , feel free to send a pull request.
>
> Hope it helps you. 

# Credits

### [Dhruv](https://github.com/DHRUV-CODER/)
