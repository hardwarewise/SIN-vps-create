D.I.N. Setup Guide : For SINOVATE Testnet
 

Download putty or any SSH client program of your choice from [https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html.)
 

Enter your IP information for the new VPS and click on the `` Open `` Button.
 

![](https://lh3.googleusercontent.com/5WjpANvCBAj-1CyHIli5_6cyQENg5Vtmh0Ew2leldNLkaMMeCQMiTd3BxB19P0d4e9WH9iHP0Mdcqd4buijIryeJIEt43oilYzHzuQEk_is0f-35xp9d1sgQg3UzqYUwfI0o0aNg)
 

Enter your username as root and enter the password given to you.  
Some VPS providers may ask you to change your temporary password immediately.

![](https://lh3.googleusercontent.com/Wo5EnBgUk-yQWXrj0llxlAHFYTimvpWKmWJMWKQ9xW-AuLLh5oItvj30oncXcdWIawL1UwAr--8R2B6Qx9nOeyjwS0KrEIYSUlNz020JDj8JPEvJ2PrLB4QN0yjO7aMinBHraTPj)

![](https://lh6.googleusercontent.com/vVsgYDUDGAGCJg6lhebnclMGhml9aOlc0kVAD03aF9VZZQjJd3xySiCyN7VnY0G46gS0NP1DL5B3K06SM6XaBhrQ-LGvCsI05OpxlPqtQQJz39IUr8a99JE1tiVlEna8e4I8ltRO)


Enter the following command to download the installation script. Please enter the code as a single line.

wget -q https://github.com/hardwarewise/SIN-vps-create/releases/latest/download/sin_install_vps_noroot.sh

![](https://lh3.googleusercontent.com/1xLqLyFK0E3pAVKq15MroyfIzW1I82DvHsRt1HhpfcrdLG3I5o-RcAx8P_GUYKn4ufF_LvfBupEmKK_Z6y5SYzwS4uROmm4unK_3924tbPlRVPJUOkXR2Xj3FoVoslBzhWDX4kvH)

Enter the code below for authorization after the script is downloaded.

chmod +x  sin_install_vps_noroot.sh


![](https://lh5.googleusercontent.com/_edPajr_rnlM2XCeML_SysvhEDFyA84gYlq2Dd3wuMHsBggQ9GBMujKH5ioN8hPwvSEcukSYjnwsR7H599n3g1EW3gOXzqHTq4if1_dChUfDRDtwR6UfWZrfBIPrthOzFfPtvAJB)


Enter the code below to run the script.

./sin_install_vps_noroot.sh


![](https://lh6.googleusercontent.com/nn0tgrojGm5d2bMbUEmXxdgXUn5mtqrFY8GcVpLeWrawn4fm4dIg1gWxJ3dnGs2FCwWIlWrfigjJ0-nOa7vTlQCORWkhaTXKRNWjEsmwjpmFewxOBsc9Z0kTX8HlRbJQeYMT8aL_)

Setup will ask for a username. If you hit enter, it will name the default sinovate.  
In our example, we used the name testuser1.

![](https://lh5.googleusercontent.com/7exjl-ISeczWhy0TjKqV4nxO-ee56cBW3u_ku_cpgs4_enOGLhGX9UuvuxYHra--LUnl_ORnB3ZT3gxaQodvJlYZU_oxlEeeT2p-5JHgFAZWgr3D6Tj-ahn_iBc1dJuIAWiJywlF)
  
At this stage, the installation will ask you to enter a password for the new user. Please choose a strong password and do not share it with anyone.  
  
The script disables root user VPS access for security.


![](https://lh4.googleusercontent.com/PpebdEeg5CtEqqPd9zISdgYdJ3FM8as_HpWBqPynS7rzEZ1L-H7rdODuyLKvLOYmIahg9JdgVXsrVWi-NBbN0Eu3646oFsG_8M-AAwL4jFnFNVA4jhtDlI7gHANbzFxaVwrUkkLu)

![](https://lh3.googleusercontent.com/C1VaohpWclC2HEATzFJbQya8U_qE2LKgSe2kMLl1RrQVoQwZ6qC1xkQFQizjIsh8sZdcDMJ7EHrIGTYUCty5s_gexpdRNQbPFgwXBDWDYdPV53l7H0ZdIpcZ1OFSj1S3PrjO6QaH)  
  
It is completed in 5-10 minutes after the installation starts. Please be patient.



![](https://lh4.googleusercontent.com/NtQX_MWgcGqCyb-FMKBebOjsGxD7Evl5yNWqE8L-drmimYtbNenZXGLEPN0rOsMZ24ji-etMD3WY4XRjqY_1NmJYwqrJ3dUSNOs5sbaErdMw-8vS0_5uAUVPiFdJnv3PRhV4qjpg)


At this stage, the SIN daemon runs automatically for the first time.  
Also, the private key given by VPS is imported to the address given by VPS.

![](https://lh3.googleusercontent.com/1_k0OGIDlCOM42Mr5R86Tc33JjU8HV57L9uNaaDXK_RBtFK83BTvanVJJk-SYtHJClrUgoVFy0f87U7y2tXkQsF9FSAE7FU-XpBbyjUv_4fVPER7FHPFTQjeyl-eeYxTdPlSktxp)

  
When the installation is completed, an information screen like the one below appears.  
  
Please save the given keys and address information. You can do this by choosing with the mouse. PuTTY and similar programs also copy the selected area to the clipboard. This information will be required in the later stages of the installation.

![](https://lh3.googleusercontent.com/v2fPGbd3P7l14DsAyU0kQ3A_iWS8n2OifqoRL0Gyd9_SXFGIgDPRePrdMoUrRhI6F6zktQzxHc2jJJJxOo_rdQ6Y0UWjibbod_IlsrGlV98ZxwJG-Rm1jCyBmiG4wI52bjC5cius)

![](https://lh5.googleusercontent.com/D9avRcWOy9X_8Yu5sRrbW0hhCpWISUfozDwvu5eErERj4otDGidsK2AfBoQHcJkV0jOcN2qlhUNGv8qtFqwCVR8uxVI41IaoLh2CXMSsB3i6Ky8RkjlcFn3ntdUmLbSwnsVEXtwS)


![](https://lh4.googleusercontent.com/RZ_N86OXKGWc2AqLaMd-mBDubqTRmZM0vvbKGRUEpI287v3lUTvx9bGRqKwcYb86kVvpdFKozMJzkD_rjoKoUGSfXAdZTlkTd6LnhCV2vZOx6ZeeGwTev2s34sPNg5nMoLMrGukT)

reboot


Return to your control wallet and create a new receiving address.  
In our example, BIG D.I.N. we will create.

![](https://lh5.googleusercontent.com/wTvnWOXEALGjjVTuFG_uEtyhwDTzgQ6qDXsRMo1WAEH2GpeuEDshtOiURMcvAMo0gTGEyEYmR272ud3PY2EU8UH3SzDV5gwlrK4ki4D78Mo86q4KINmMANq_dVphAs3GcNLGE4Hm)

![](https://lh6.googleusercontent.com/Ri5BtriwLci3B9ZKRdMAdd1cY9_jF2HIWwsBIAcAFCeii-dnnOOVfI70qnsD8Tg45dM80jaSt1qW0YKSg_-I8P3ZAR4wRCMRYg1nYZaFdUJNQc9LcHuZDay_N6fgOVnrgFjJqtSE)

Copy the new address you create and send it exactly 1 000 000 SIN to this address.  
  
BIG D.I.N. 1 000 000 for

MID D.I.N. 500 000 for

MINI D.I.N. 100 000 for

You should send.

![](https://lh4.googleusercontent.com/Z_Lw5uUKSxlo7vB0ocR6ekH7RkVF9g_fgFkVvvuHc4D3oziWDubTNayG-0PY0n6rkYzxJIR8efi-ubupKk7VvmM72pxcS_ZMpluk-LqGVA6u7GoDoGxSgqDV5Dr85vgAQY_vrx6n)

![](https://lh6.googleusercontent.com/U4b-o_P7ceYBxeDmtdNEQyCVSKvMgin_8CQ04W_jnm0c3xIHyGLLlcyiPsnTtLaLpKLpwX4xT4KqMJx6JuQlze3m_1eCkQu-odmRDt08_PrgWSoo1aDffVRQ66ebDv4eo6q5G-Q2)

![](https://lh3.googleusercontent.com/NdYOt5yF-F7XHRtJELHiuAYgx1u0IWkvKEW5ZsT8d5W-f6uItFkl3cHb7Yrfu6nUU4eVjjggp8SgHEtmtXmGmU1vlRbwr48KVlVUXMG_Z1KsRyLYtv3lxNkprBw6QkrxuNcWh9AC)


![](https://lh6.googleusercontent.com/Uyq2ciU1m6fD0AL4YgmsEsWscsjJMBr6AodJWtqA5QIwxO-N9f0dP6SJYaJz3g9yyRgoSBaOWCO4jWMv_O_NCyGAjhXvgDtXzp33e8RNOzsXMVVf7KWVomwDAXat1cHIN2QaZvH-)


walletpassphrase [passphrase] [timeout]

  

![](https://lh4.googleusercontent.com/vJ8oy-ATier0CnKzeMrTNcxxe_ni0VZSRqcxEZo81mlVhOfucMc4DYlDtxqaSc4az7E6MSvQgDAxEFRDr_BBWZYTTR0WilhBC4U49f23zvU8J2lF7i65XO604wOdKKruIrjsc7uW)


infinitynodeburnfund [YourAddress] [Amount 1M / 500K / 100K] [YourBackupAddress]

![](https://lh5.googleusercontent.com/TUcksOjmWBZUWDj8Dg_I5Vhk0to1SThS3AqPAOPh9QgDIdiIsaDGpnpcSKnA7PmWysAPfGEUnOZ88jo0rGAkE7snq9hyEDFK4i9t_6JGbAdK8kRnHuVzWSgVFx55NYPLL4RLvOFg)

![](https://lh3.googleusercontent.com/F7RsNTGrotLg1w5aFRUnXruBj1SWAvT_w57xvbuTa9hONQM2aJBEads5s1jBqDRT8BV8z8BhpuyXI6dif_-B6Oz1RWyM-ccLWxXz3axs-te4FNGvLsbiPY4Epuk6N34beuZlzWC5)


![](https://lh4.googleusercontent.com/_ldMREIm59dbGnWu9sI_WVnqeIYqjs8tCGFfwB2c7d4ZHMwT2CuYMsY_PoTkYINLUkuTbyeUmVczVFAsu50BpFSQaDWRq3QrdbsroykLD1oPVu9vEUMM7z7rxn2cx_QoezK-sSz_)

![](https://lh6.googleusercontent.com/0zoosB9X4_JrvMRSzmFEWazUa9YAmdL9cQvfS3Sk1ayfdL5FWZv6M8xQ6mPX2_97gJ4G4afWamx1xMVaaUSdrVD80mP8A746iBkDSi_x0Hdog0PGoKZzdJ0uHvVzU1ym-Jak_p2h)


![](https://lh3.googleusercontent.com/qg8XJ6O4_2oA-SwXFMGNwVyWv3TfuQqphPh_MMlHyoCztpnDCM0TZucVLW3qHXxxBYDvpJehiPvN8gSkUG98KhUFUc8HEGu64I49IMoB5UKzTXzDgXpTYpCdZUqwFVxqwxID_gN-)

![](https://lh4.googleusercontent.com/D-pzXkmy9J8o-Ib4RRz9P-E56K9f_nkud-tGx_D6OUsxgYSr8Oi5KQ-sGdZq61ittQuE80v7_UJdWb49nnTc1TFILuf6ugBxmkfD76oasnh_Nfgg0Ha90psY2mluHNP5QeI3oNQw)


![](https://lh5.googleusercontent.com/-96OAgfyyJuO0jiz1X4U9-wbFCA7tGvuhxtRtm4eftwGiPdjlWCV4Z5hOXItXj0pxgg8BIJbh7ZQ6_dCRNBa1WZI_S5V1Kz8MIiMt0Eh0jJwMU931uRDcIzQlrfRg6SYoOuudO5U)


infinitynodeupdatemeta [Owner address] [node PublicKey] [node IP] [first 16 characters of BurnFundTx]


![](https://lh6.googleusercontent.com/wp6rPtiuRNOM3Vn3RZK_4yxKIO9gjK-cuOdpXJW9wUhU5ZRO8FsNmIMWo2LV5Alrj_sH-paR20xsYvyYjgBE1DPkYCQQCksl9cJwMQemdwf8ueEWydBacgWTiNEMO-h2CK19tVDj)

![](https://lh5.googleusercontent.com/fU4rq0BEjjeQDPgVnaKOzF90ZH-PH-XBf55V6MvaUD4pC-9LNpgtc_dcIsQIpw6fHz3ZMShWm1YYIsQAQzyEX3DNmokjz0VxNrh-9sAVg5BQejCIM1gZz6qgOzCepCSaZTJsdx58)  
  
![](https://lh6.googleusercontent.com/nV0kTB3yBz_dD8_n31lbxIK8qfbakkjZs5UO80HBRxS1agqlRLlw7PK04Qr8GoB8MT8lLGeFGw5aD01417jsguaO0wyKRtARsF5_OqrsWqizJDL1kMpSXguMpo8eFh0Lsq5Kadda)
