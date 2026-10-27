from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/categories")
def get_categories():
    return {
        "categories": [
            {
                "key": "skin-acne",
                "name_ar": "حب الشباب والبثور",
                "name_en": "Acne & Blemishes",
                "desc_ar": "تنظيم إفراز الدهون وتقليل التهابات البشرة",
                "desc_en": "Regulate sebum production and reduce skin inflammation"
            },
            {
                "key": "skin-pigmentation",
                "name_ar": "التصبغات وآثار الحبوب",
                "name_en": "Pigmentation & Dark Spots",
                "desc_ar": "توحيد لون البشرة وإزالة التصبغات بالمكونات الفعالة",
                "desc_en": "Even out skin tone and eliminate dark spots with actives"
            },
            {
                "key": "skin-barrier",
                "name_ar": "تضرر حاجز البشرة",
                "name_en": "Skin Barrier Repair",
                "desc_ar": "إصلاح وترطيب وحماية طبقات الجلد الحيوية",
                "desc_en": "Repair, moisturize and protect vital skin layers"
            },
            {
                "key": "hair-loss",
                "name_ar": "تساقط الشعر وفروة الرأس",
                "name_en": "Hair Loss & Scalp",
                "desc_ar": "تحفيز بصيلات الشعر وعلاج مشاكل فروة الرأس",
                "desc_en": "Stimulate hair follicles and treat scalp issues"
            }
        ]
    }