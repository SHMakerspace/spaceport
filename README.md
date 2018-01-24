Spaceport: Open access control
==================
Spaceport is inspired from the great [Carontepass](https://github.com/torehc/carontepass-v2) , although it employs similar hardware and paradigms, the software has been fully rewritten and hardware aspects have been refined and redesigned.

Spaceport is designed to be an access control system by means of low cost RFID tags. Developed by and for **Surrey and Hampshire Makerspace**, it is ideally suited for all makerspaces and similar. 

It’s design adheres to the following principles:

- Open source
- Open Hardware(ish)
- Low cost
- Self contained, whilst exposing actions for other distributed applications to interact with
- Easy to implement and use

Spaceport is made of several components, employing the same client-server paradigm as Carontepass; clients consisting of **WEMOS (ESP8266)** wifi micro-controllers, which reads RFID tags via a **RC522 RFID reader** and controls a lock after authorisation from the server via a REST API request and response cycle.

The client connects of a Wifi network of the administrator's choosing to perform it's API access requests.

Client
-------

The Client consists of 2 PCBs (Spaceport controller and Spaceport reader) these allow mounting of the off the shelf PCBs (Wemos and RC522), power management (a 12V DC power supply is the only power input required). Control of the door lock is via MOSFETs (configurable for a fail open or fail closed door lock) and connectivity between the controller and reader (RJ45). 

The PCBs are designed in EagleCAD and are available in a separate repo here: [PBC Repo](https://github.com/SHMakerspace/spaceportpcb)
 
The choice of 2 PCBs with RJ45 connectivity was taken so that the controller can be easily mounted in a location that cannot be accessed (and therefore not tampered with) whilst the reader can be mounted in a more open location. RJ45 was chosen due to it's low cost and relative density of connections.

The controller and reader both have a 3D printed case and laser cut (although could also be 3D printed) lid. The casing has been designed in the free to use software Autodesk Fusion 360. Designs are available here: [Controller](http://a360.co/2D648rg) [Reader](http://a360.co/2k06he2)

The client firmware has available in a separate repos here: [WEMOS firmware repo](https://github.com/SHMakerspace/spaceportclient)

![PCBs](https://lh3.googleusercontent.com/g8-eCmGsM58siEUREAJQxgl26oSliJ-2NyPW6FOMdzvt_YHkEdBsc1cU5JWBC_lprGO7F8F3ThcDM_IRJHGNp3lH1DRBhw5yG0vpXb5wSVXzZ42BomTwUZnGATMCjlY0k3_H5Yt0mAFraEeLzEeb6mTGwxtiBvsvU_cfevI-thxgwVujKMEgD9XBA_XJLVQzAwf8d0RPYAYVQGPrfWlY_laGTWThU_avMRDu92ImBItWaK0IjaGnYVnYxnggVs4SwaaNuJpahqiSyLMhoGB9ldxzHuoans6Ikqi9QLDSBORbWw5_zX3XY1whjGAgJjJJpDNsrc3af8auh3d60lcXBpei0LkKFs6z0Sxrel0nS1Bge0rzmwRRYahMxtU5Eh58kv9pTjtxhfeFLGm6uNuZOdXpnKjWtL1RWKSHmZ5YliH4tDq5j5zixpuK-VZTfNrQDeJjGsRYbCt8ifrUpd-hSE3mDRIExDh6mEqFzbzMBJwEUJ4LLboPXsA984RTtAiPNChG5fLxXXG1uoGWbgZUuVMKg13lt4O5OBFcVLWfw3khb7lOyGHchTCrdPyaUzFsNmHRzKGXfn6DehrlLwFKzJGggAWy8papKypQXUm6yjXvfaEbS-d9mdQl7Ckjdo1TqbX3iGQynoajx5urhemQ9bXHlX8NNMWd=w1257-h711-no)
![PCBs connected](https://lh3.googleusercontent.com/SmRcyuGPhfHDCFuXUq3HyAAxzpvi46Vhj20UENNceX2iJmsTpmnlcxX0mSTV7oRemNxiCAciB0nkxVafn33NYWc1HM0UNIRGA0VF3eEF7kA2_lkThV6u29iYwtv58UHvreQ84RdqeEWWulvHeNNJjnFHg_jtr67aVf3ZV-DUsfOmCH1r2S6oP8TD1sB4QGI1pXwvafTJB06vM0nX8yS5zvueL55ybjpmloJzJE-IEJiSXSPYPqkAAs7Nbkx4VlgX-7DFz5PgABHwOgCT3eAdcpAJAE3n3BzAAE0b7GR6lzaCRFfLjwI62amUobbnEfVLvyD1ZQIFKFmfiGNQiYndCQ0hrGDRzkn4H-sUfZFoC_l35k1faOcroK_PJyuLEWOl0WVtaefAGl3kLLiFtJ6ve14sBVBkDZM1N706B_lrCuvK4th9nXB6tgH_6QzW_GWjhQnYI3Xm5TCzS54YNJXsRCGFRwXm47n8eHd8Lbt9TZvyDGAlNPTkqt6nTkWqigKjnnlkVO9D8STUuHtQq38kXY4hXW33JdA7hyP5OEGOFgytJzsq30v9VIxgXpxPrPjCRB4-wBIoPLbyjydu1hVe5mOkrkVyWeGX-5OuvFs-pT_HbesU5BQzoTBSnDO6zgx5ccHTq1Gu1mE2ZqL9qXxVkH4OmUbEUnBB=w1257-h711-no)
![PCBs in casing](https://lh3.googleusercontent.com/vOZHs0g38h1XdOtqBPBcfA0klL8pLzkZKdDBBTxyE5ixQoRTXagYHA0fLNtRR2rmN7y04_YJt7Ta6bYWGVqg7kTKKRfl-xxmX073LmvRIKBmzaJOUsvYTIy-lH331EfX50_hlWbdnzBPIXLwupwjjjH3H9TaSFKqqEGNd6tLwzGF8_BateV_IgPAmo8iEPYiiI_jfJTcap6CIT5w-71ndXMA7yiKlUbmUanMoEGJRAiwyt2Jg-2k7Ke3-HXjXMzDoZvmqbwlZYKz2JXOT-exnOqbHrav7lRoPmdPyLxFmE2If_QOWHqLl5-9uIZ3jF3KpGcJZA19Pc5ti057UByP91uyNgX8Nt7HCpUdn_IMeLRFRhdtvInACVOiSHnEBgrv-1kJF5i0MvdId0ExS0EMFR8jqzr7iTq8a4EOSYvLCe_y0BCGglyJuDZsH50FfPAIL86EBkm2sLpcij7sMQrKpGzfNbJJ8Zm7rkjsQAgw-94hZDZG3iesHFPv-EqeYOIe7KtlN1z0UvxmzYys3l_uzYN76BhVu4ZQ7qq1FFTQsfAZRRIFlpbC2TXv7eSsTL6H8RzK3wFSmLK3Fdr0DRTHI5odQDcfhBV-hnnjCxDnOvGYaF4v_2RXruh14th-6ISnTjN0zkg1m7PmmUqWatSthC7nb44pEAZT=w1257-h711-no)

Server
------
The server Spaceport application is developed in the **Python** using the **Django web framework** and the **Django REST framework**.

There is very little custom UI, Spaceport relies heavily on a tuned configuration the Django admin interface.

The core of the data model is the following: **Users, Tags and Security Nodes** (The first 2 are self explanatory, security node is to be considered as a single client, as described above). A user may be active or inactive, they may have a number of tags assigned to them and the user can be given permission to access to a security node.

A client can make an API request containing it's security node ID and Tag making the access request to the server for authorisation. The server will check the user the tag is assigned to and check if the user has the permission to access the security node, it will then respond to the client to grant or deny access.

There is also an API endpoint to register new tags, ready for a Spaceport administrator to associate with a user.

Spaceport emits all valid access requests to a **MQTT server** of the administrators choosing, this is to fulfil one of the core Spaceport principles of being self contained, whilst exposing actions for other distributed applications to interact with ~ this allows anyone to create all kinds of weird and wonderful applications that react to Spaceport actions without having to touch the Spaceport application (We have visions of all kinds of bells, whistles and das blinken lights when users enter the makerspace).

Currently there is simple application that emits states to a Slack channel as Surrey and Hampshire Makerspace use slack as one of their communication mediums, repo for the slack app here: [Slack Client repo](https://github.com/SHMakerspace/spaceportslackbot)

The Spaceport server was developed on an Orange Pi Zero due to it's low cost and inclusion of ethernet connectivity, but it could run on just about any linux computer (Including Raspberry Pi).
![Oraage PI]i(https://lh3.googleusercontent.com/Q3IvxD_sLk-yX-Jeg-zwOYFnuL9tn_LTQZdQwab-DIJAJQjXO5tDsj6RjZpb4BQB7oscVeHOWMIsiFc30tKNHFJedTzcDs7wX_kNdqMF9lfMGiFbPOC_CysgNziCoCUHNVK6gkfLnhUJjrK0rqtwtrKwwwApQ9y6M_SjEUkb4LIGSwvUmCd2hdDHF_KRGTej68Ar2lKo8gKUOKbSngZWtcqIyf8LUvY_ja_7Ga8JOJXCCm7n5Z0f74kvEX15M4km-hj2Er_sf289BA7RAslhS0-R2HiKeuo5280VYv_Nwo7WdlG9GIkUoi7A7m5M0axJUC415qtWcnsvbT3miUgEOYV2sWWg-p5WxnKzVGVhTfIO5N6sysUqqCYJjFfYAojFEZC_pOkRhuCG-Lq5cq9tMN_TabYupqGc4-jqvui1sAuLemr585KPiSw6dgSIG-S4EiyC2m3yzgsok-lcRonOMclMZEL20IhCBwDjf6NUaC0bAyZRu0fIvC73Q6Ik1lspasv7fkDiwvdrqceDLEayf5beIFgMNjEGsHfCKIojiesdrfLBGMuXAWw2W8Y0yPmMMyDuKx81svL23lWFlIK7BstBxtuDTG-NAlfIL7brg0SghmasPzvSo7CbGCxKm1TsGOPAIrdtqAAnXxv-gv5djASS6AZ6ZQ-F=w1270-h719-no)

Links
----
- [Documentation](https://github.com/SHMakerspace/spaceport/wiki)
- [PBC Repo](https://github.com/SHMakerspace/spaceportpcb)
- Case Design: [Controller](http://a360.co/2D648rg) [Reader](http://a360.co/2k06he2)
- [WEMOS firmware repo](https://github.com/SHMakerspace/spaceportclient)
- [Slack Client repo](https://github.com/SHMakerspace/spaceportslackbot)
