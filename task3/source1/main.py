import time

from fastapi import FastAPI

app = FastAPI()


@app.get("/fuel-stations")
def get_fuel_stations_data():
    time.sleep(4)
    return [
        {
            "id": 1,
            "coordinates": [55.797817, 49.130638],
            "number": 1,
            "address": "ул. Федосеевская, 36, город Казань, Респ. Татарстан, Россия, 420111",
            "image_urls": [
                "https://www.google.com/maps/place/%D0%94%D0%B2%D0%BE%D1%80%D0%B5%D1%86+%D0%97%D0%B5%D0%BC%D0%BB%D0%B5%D0%B4%D0%B5%D0%BB%D1%8C%D1%86%D0%B5%D0%B2/@55.800514,49.1118931,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipMe9sAgmKaxew34qEx0ZyAKWQunzZs2shCOZ1cn!2e10!3e12!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipMe9sAgmKaxew34qEx0ZyAKWQunzZs2shCOZ1cn%3Dw130-h86-k-no!7i3901!8i2574!4m16!1m8!3m7!1s0x415ead2b7caccd99:0x7fcb77b9b5ad8c65!2z0JrQsNC30LDQvdGMLCDQoNC10YHQvy4g0KLQsNGC0LDRgNGB0YLQsNC9LCDQoNC-0YHRgdC40Y8!3b1!8m2!3d55.7878944!4d49.1233294!16zL20vMDFjcjI4!3m6!1s0x415ead3ec12abebd:0xc937e3a3bfa875f9!8m2!3d55.800514!4d49.1118931!10e5!16s%2Fg%2F121h835y?entry=ttu#",
                "https://www.google.com/maps/place/%D0%94%D0%B2%D0%BE%D1%80%D0%B5%D1%86+%D0%97%D0%B5%D0%BC%D0%BB%D0%B5%D0%B4%D0%B5%D0%BB%D1%8C%D1%86%D0%B5%D0%B2/@55.8005515,49.1118431,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipNSOHjSfXidO2213G8R04otSiFHzZjysiSvvbo-!2e10!3e12!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipNSOHjSfXidO2213G8R04otSiFHzZjysiSvvbo-%3Dw203-h203-k-no!7i3024!8i3024!4m16!1m8!3m7!1s0x415ead2b7caccd99:0x7fcb77b9b5ad8c65!2z0JrQsNC30LDQvdGMLCDQoNC10YHQvy4g0KLQsNGC0LDRgNGB0YLQsNC9LCDQoNC-0YHRgdC40Y8!3b1!8m2!3d55.7878944!4d49.1233294!16zL20vMDFjcjI4!3m6!1s0x415ead3ec12abebd:0xc937e3a3bfa875f9!8m2!3d55.800514!4d49.1118931!10e5!16s%2Fg%2F121h835y?entry=ttu#",
                "https://www.google.com/maps/place/%D0%94%D0%B2%D0%BE%D1%80%D0%B5%D1%86+%D0%97%D0%B5%D0%BC%D0%BB%D0%B5%D0%B4%D0%B5%D0%BB%D1%8C%D1%86%D0%B5%D0%B2/@55.800514,49.1118931,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipOgxFKr7lJLrQuYST4rFvn8IDBdN5y6eEKs1doj!2e10!3e12!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipOgxFKr7lJLrQuYST4rFvn8IDBdN5y6eEKs1doj%3Dw203-h134-k-no!7i4543!8i3019!4m16!1m8!3m7!1s0x415ead2b7caccd99:0x7fcb77b9b5ad8c65!2z0JrQsNC30LDQvdGMLCDQoNC10YHQvy4g0KLQsNGC0LDRgNGB0YLQsNC9LCDQoNC-0YHRgdC40Y8!3b1!8m2!3d55.7878944!4d49.1233294!16zL20vMDFjcjI4!3m6!1s0x415ead3ec12abebd:0xc937e3a3bfa875f9!8m2!3d55.800514!4d49.1118931!10e5!16s%2Fg%2F121h835y?entry=ttu#",
            ],
            "additional_services": [
                "Замена шин",
                "Замена масла",
                "Гаечный ключ",
                "Подкачка колес",
                "Пылесос"
            ]

        },
        {
            "id": 2,
            "coordinates": [55.794126, 49.120886],
            "number": 2,
            "address": "ул. Дзержинского, Казань, Респ. Татарстан, Россия, 420111",
            "image_urls": [
                "https://www.google.com/maps/place/%D0%A7%D1%91%D1%80%D0%BD%D0%BE%D0%B5+%D0%BE%D0%B7%D0%B5%D1%80%D0%BE/@55.7942622,49.1215372,3a,75y,90t/data=!3m8!1e2!3m6!1shttp:%2F%2Ft2.gstatic.com%2Fimages%3Fq%3Dtbn:ANd9GcRFNb3Apy2J6JIarNgLZ49YFhF16hXHdWe9jQyX2Eo1ijh61Y68!2e7!3e27!6shttps:%2F%2Flh3.googleusercontent.com%2Fgps-proxy%2FAMy85WK7sY8eSZZY8Vt77SvsoFs78V55HuQvsQk8v0RnwDyA4iJSayJfirH1urH8MJ8PE6Rn8kfeGUMMtddS790xvMuKDdtPld7iKjbbGnsz-Qe6XqH1HMllu4MTdS7p4ngtBm9ZjvfHWpAAu1hfLcGRy8Et9D2Z_73AK9ZFGcvLGo0QlYBhJ6paKGIuMQ%3Dw114-h86-k-no!7i1080!8i810!4m16!1m8!3m7!1s0x415ead2b7caccd99:0x7fcb77b9b5ad8c65!2z0JrQsNC30LDQvdGMLCDQoNC10YHQvy4g0KLQsNGC0LDRgNGB0YLQsNC9LCDQoNC-0YHRgdC40Y8!3b1!8m2!3d55.7878944!4d49.1233294!16zL20vMDFjcjI4!3m6!1s0x415ead1670bf398f:0x96b04bb5c4da65ac!8m2!3d55.7939678!4d49.1208442!10e5!16s%2Fg%2F1hb_dhnpk?entry=ttu#",
                "https://www.google.com/maps/place/%D0%A7%D1%91%D1%80%D0%BD%D0%BE%D0%B5+%D0%BE%D0%B7%D0%B5%D1%80%D0%BE/@55.7939678,49.1208442,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipMfiqygu6B6S7QDVWu7JVeJLCUpGz11p8gLwFDb!2e10!3e12!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipMfiqygu6B6S7QDVWu7JVeJLCUpGz11p8gLwFDb%3Dw203-h152-k-no!7i4032!8i3024!4m16!1m8!3m7!1s0x415ead2b7caccd99:0x7fcb77b9b5ad8c65!2z0JrQsNC30LDQvdGMLCDQoNC10YHQvy4g0KLQsNGC0LDRgNGB0YLQsNC9LCDQoNC-0YHRgdC40Y8!3b1!8m2!3d55.7878944!4d49.1233294!16zL20vMDFjcjI4!3m6!1s0x415ead1670bf398f:0x96b04bb5c4da65ac!8m2!3d55.7939678!4d49.1208442!10e5!16s%2Fg%2F1hb_dhnpk?entry=ttu#",

            ],
            "additional_services": [
                "Замена шин",
                "Мойка"
            ]
        },
        {
            "id": 3,
            "coordinates": [55.794126, 49.120886],
            "number": 3,
            "address": "ул. Университесткая 1, Иннополис",
            "image_urls": [

            ],
            "additional_services": [

            ]
        },
        {
            "id": 4,
            "coordinates": [44.816068, 20.460431],
            "number": 4,
            "address": "Трг републике 3, Београд, Центр",
            "image_urls": [
                "https://www.google.com/maps/place/Republic+Square/@44.8162551,20.4603199,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipOlGm2qJnBIoQaj-t23b6m1mAStVNMBtIuSMWqB!2e10!3e12!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipOlGm2qJnBIoQaj-t23b6m1mAStVNMBtIuSMWqB%3Dw114-h86-k-no!7i12000!8i9000!4m16!1m8!3m7!1s0x475a7aa3d7b53fbd:0x1db8645cf2177ee4!2z0JHQtdC70LPRgNCw0LQ!3b1!8m2!3d44.8125449!4d20.4612299!16zL20vMGZoemY!3m6!1s0x475a7bb00177ef0f:0x448846444afd8bbb!8m2!3d44.8161885!4d20.4603829!10e5!16zL20vMGJtdjE1?entry=ttu#"
            ],
            "additional_services": [
                "Пылесос",
                "Замена шин"
            ]
        }
    ]
