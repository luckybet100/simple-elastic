from elasticsearch import Elasticsearch

from node import get_es

data = [{
    "title": "Государственная Третьяковская галерея",
    "city": "Москва",
    "region": "Москва"
}, {
    "title": "Государственный исторический музей",
    "city": "Москва",
    "region": "Москва"
}, {
    "title": "Государственный Эрмитаж",
    "city": "Cанкт-Петербург",
    "region": "Cанкт-Петербург"
}, {
    "title": "Государственный музей изобразительных искусств имени А. С. Пушкина",
    "city": "Москва",
    "region": "Москва"
}, {
    "title": "Тульский государственный музей оружия",
    "city": "Тула",
    "region": "Тульская область"
}, {
    "title": "Русский музей. Мраморный дворец",
    "city": "Cанкт-Петербург",
    "region": "Cанкт-Петербург"
}, {
    "title": "Государственный центральный театральный музей им. А. А. Бахрушина",
    "city": "Москва",
    "region": "Москва"
}, {
    "title": "Музей современного искусства 'Гараж'",
    "city": "Москва",
    "region": "Москва"
}, {
    "title": "Государственный музей-заповедник С. А. Есенина",
    "city": "Москва",
    "region": "Москва"
}, {
    "title": "Музей Фаберже",
    "city": "Cанкт-Петербург",
    "region": "Cанкт-Петербург"
}, {
    "title": "Музей искусства Cанкт-Петербурга XX–XXI веков",
    "city": "Cанкт-Петербург",
    "region": "Cанкт-Петербург"
}, {
    "title": "Центральный выставочный зал 'Манеж'",
    "city": "Москва",
    "region": "Москва"
}, {
    "title": "Музей истории государственных бумаг России Cанкт-Петербургской бумажной фабрики 'Гознак'",
    "city": "Cанкт-Петербург",
    "region": "Cанкт-Петербург"
}, {
    "title": "Музей Москвы",
    "city": "Москва",
    "region": "Москва"
}, {
    "title": "Музеи Московского Кремля",
    "city": "Москва",
    "region": "Москва"
}, {
    "title": "Куликово поле",
    "city": "Тула",
    "region": "Тульская область"
}, {
    "title": "Всероссийский музей декоративно-прикладного и народного искусства",
    "city": "Москва",
    "region": "Москва"
}, {
    "title": "Государственный музей-памятник 'Исаакиевский собор'",
    "city": "Cанкт-Петербург",
    "region": "Cанкт-Петербург"
}, {
    "title": "Музей Победы",
    "city": "Москва",
    "region": "Москва"
}, {
    "title": "Государственный музей-заповедник М. А. Шолохова",
    "city": "Cанкт-Петербург",
    "region": "Cанкт-Петербург"
}, {
    "title": "Музей-заповедник 'Царское Село'",
    "city": "Cанкт-Петербург",
    "region": "Cанкт-Петербург"
}, {
    "title": "Государственный музей искусства народов Востока",
    "city": "Москва",
    "region": "Москва"
}, {
    "title": "Музей современного искусства Эрарта",
    "city": "Cанкт-Петербург",
    "region": "Cанкт-Петербург"
}, {
    "title": "Государственный научно-исследовательский музей архитектуры имени А. В. Щусева",
    "city": "Москва",
    "region": "Москва"
}, {
    "title": "Государственный музей-заповедник 'Петергоф'",
    "city": "Cанкт-Петербург",
    "region": "Cанкт-Петербург"
}, {
    "title": "Всероссийский музей А. С. Пушкина",
    "city": "Cанкт-Петербург",
    "region": "Cанкт-Петербург"
}, {
    "title": "Еврейский музей и центр толерантности",
    "city": "Москва",
    "region": "Москва"
}, {
    "title": "Открытый музей Cанкт-Петербургской академии управления и экономики",
    "city": "Cанкт-Петербург",
    "region": "Cанкт-Петербург"
}, {
    "title": "Галерея 'Кино' г. Москва",
    "city": "Москва",
    "region": "Москва"
}, {
    "title": "Музей гражданской авиации в Cанкт-Петербурге",
    "city": "Cанкт-Петербург",
    "region": "Cанкт-Петербург"
}, {
    "title": "Дом-музей В.И. Ленина ",
    "city": "Казань",
    "region": "республика Татарстан"
}, {
    "title": "Центр 'Эрмитаж-Казань'",
    "city": "Казань",
    "region": "республика Татарстан"
}, {
    "title": "Исторический парк 'Россия – моя история' г. Казань",
    "city": "Казань",
    "region": "республика Татарстан"
}, {
    "title": "Владимиро-Суздальский музей-заповедник",
    "city": "Владимир",
    "region": "Владимирская область"
}, {
    "title": "Исторический музей во Владимире",
    "city": "Владимир",
    "region": "Владимирская область"
}, {
    "title": "Собор св. равноапостольного князя Владимира",
    "city": "Владимир",
    "region": "Владимирская область"
}, {
    "title": "Владимирский музей 'Старая аптека'",
    "city": "Владимир",
    "region": "Владимирская область"
}, {
    "title": "Исторический музей г. Владимира",
    "city": "Владимир",
    "region": "Владимирская область"
}, {
    "title": "Национальный музей Республики Карелия",
    "city": "Петрозаводск",
    "region": "республика Карелия"
}, {
    "title": "Музей изобразительных искусств Республики Карелия",
    "city": "Петрозаводск",
    "region": "республика Карелия"
}, {
    "title": "Музей истории народного образования Республики Карелия",
    "city": "Петрозаводск",
    "region": "республика Карелия"
}, {
    "title": "Музей истории Культурного центра МВД по Республике Карелия",
    "city": "Петрозаводск",
    "region": "республика Карелия"
}, {
    "title": "Сочинский художественный музей",
    "city": "Сочи",
    "region": "Краснодарский край"
}, {
    "title": "Литературно-мемориальный музей Н. Островского в г. Сочи",
    "city": "Сочи",
    "region": "Краснодарский край"
}, {
    "title": "Музей истории города-курорта Сочи",
    "city": "Сочи",
    "region": "Краснодарский край"
}, {
    "title": "Сочинский музей ретро-автомобилей",
    "city": "Сочи",
    "region": "Краснодарский край"
}, {
    "title": "Музей спортивной славы г. Сочи",
    "city": "Сочи",
    "region": "Краснодарский край"
}, {
    "title": "Музей-заповедник 'Владивостокская крепость'",
    "city": "Владивосток",
    "region": "Приморский край"
}, {
    "title": "Музейно-выставочный центр г. Владивосток",
    "city": "Владивосток",
    "region": "Приморский край"
}, {
    "title": "Военно-исторический фортификационный музей 'Владивостокская крепость'",
    "city": "Владивосток",
    "region": "Приморский край"
}]


async def init_elastic():
    es = await get_es()
    es.indices.create(index="museums", ignore=400)
    es.indices.close(index="museums")
    es.indices.put_settings(
        {"settings": {
            "index": {
                "analysis": {
                    "analyzer": {
                        "my_text_analyzer": {
                            "type": "custom",
                            "tokenizer": "standard",
                            "filter": [
                                "lowercase",
                                "russian_morphology",
                                "english_morphology",
                                "ngram_filter"
                            ]
                        },
                        "my_search_analyzer": {
                            "type": "custom",
                            "tokenizer": "standard",
                            "filter": [
                                "lowercase",
                                "russian_morphology",
                                "english_morphology"
                            ]
                        },
                    },
                    "filter": {
                        "ngram_filter": {
                            "type": "nGram",
                            "min_gram": 4,
                            "max_gram": 16
                        }
                    }
                }
            }
        }}, index="museums"
    )
    es.indices.put_mapping("museum", body={
        "properties": {
            "title": {
                "type": "string",
                "analyzer": "my_text_analyzer"
            },
            "city": {
                "type": "string",
                "analyzer": "my_text_analyzer"
            },
            "region": {
                "type": "string",
                "analyzer": "my_text_analyzer"
            },
        }
    }, index="museums")
    es.indices.open(index="museums")
    for index, doc in enumerate(data):
        es.index(index="museums", id=index, doc_type='museum', body=doc)
