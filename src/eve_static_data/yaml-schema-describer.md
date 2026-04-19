I currently have an implemetation of this that works with jsonl files, but I now prefer the subtle differences that are in the yaml dataset files.

I have a collection of data that consists of a number of yaml files.

The top level of the yamls files is a dictionary, but the dictionary can contain scalar values, lists, and dictionaries.
Containers inside the top level dict can be assumed to contain that same data type, eg. a list will only contain ints, or will only contain dicts.

I need a function that will scan each yaml file, and report the type and number of occurances of each item of data, including the top level key, such that I can use the result to create typeddict, or dataclass representations of the schema. I also need to be able to easily tell if the schema changes later. some examples of different datasets are:

```yaml
0:
  anchorable: false
  anchored: false
  categoryID: 0
  fittableNonSingleton: false
  name:
    de: '#System'
    en: '#System'
    es: '#System'
    fr: '#Système'
    ja: '#システム'
    ko: '#항성계'
    ru: '#Система'
    zh: '#星系'
  published: false
  useBasePrice: false
1:
  anchorable: false
  anchored: false
  categoryID: 1
  fittableNonSingleton: false
  name:
    de: Charakter
    en: Character
    es: Personaje
    fr: Personnage
    ja: キャラクター
    ko: 캐릭터
    ru: Персонаж
    zh: 人物角色
  published: false
  useBasePrice: false
2:
  anchorable: false
  anchored: false
  categoryID: 1
  fittableNonSingleton: false
  name:
    de: Corporation
    en: Corporation
    es: Corporación
    fr: Corporation
    ja: コーポレーション
    ko: 코퍼레이션
    ru: Корпорация
    zh: 军团
  published: false
  useBasePrice: false
```

and

```yaml
681:
  activities:
    copying:
      time: 480
    manufacturing:
      materials:
      - quantity: 86
        typeID: 38
      products:
      - quantity: 1
        typeID: 165
      time: 600
    research_material:
      time: 210
    research_time:
      time: 210
  blueprintTypeID: 681
  maxProductionLimit: 300
682:
  activities:
    copying:
      time: 480
    manufacturing:
      materials:
      - quantity: 133
        typeID: 38
      products:
      - quantity: 1
        typeID: 166
      time: 600
    research_material:
      time: 210
    research_time:
      time: 210
  blueprintTypeID: 682
  maxProductionLimit: 300
683:
  activities:
    copying:
      time: 4800
    invention:
      materials:
      - quantity: 2
        typeID: 20416
      - quantity: 2
        typeID: 25887
      products:
      - probability: 0.3
        quantity: 1
        typeID: 39581
      skills:
      - level: 1
        typeID: 11442
      - level: 1
        typeID: 11454
      - level: 1
        typeID: 21790
      time: 63900
    manufacturing:
      materials:
      - quantity: 24000
        typeID: 34
      - quantity: 4500
        typeID: 35
      - quantity: 1875
        typeID: 36
      - quantity: 375
        typeID: 37
      products:
      - quantity: 1
        typeID: 582
      skills:
      - level: 1
        typeID: 3380
      time: 6000
    research_material:
      time: 2100
    research_time:
      time: 2100
  blueprintTypeID: 683
  maxProductionLimit: 30
```

help me plan out this function, and show me some result formats.