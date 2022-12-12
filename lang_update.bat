pyside6-lupdate -extensions py,ui src/ -ts src/translations/lang_kor.ts
pyside6-lupdate -extensions py,ui src/ -ts src/translations/lang_eng.ts

pyside6-linguist src/translations/lang_kor.ts
pyside6-linguist src/translations/lang_eng.ts