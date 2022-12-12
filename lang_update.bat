pyside6-lupdate -extensions py src/ -ts src/translations/lang_kr.ts
pyside6-lupdate -extensions py src/ -ts src/translations/lang_en.ts

pyside6-linguist src/translations/lang_kr.ts
pyside6-linguist src/translations/lang_en.ts