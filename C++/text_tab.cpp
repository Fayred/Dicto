#include "text_tab.h"
#include "ui_text_tab.h"

text_tab::text_tab(QWidget *parent) : QWidget(parent), ui(new Ui::text_tab)
{
    ui->setupUi(this);
}

text_tab::~text_tab()
{
    delete ui;
}

QString text_tab::get_text(){
    return ui->plainTextEdit->toPlainText();
}

void text_tab::set_text(QString content){
    ui->plainTextEdit->setPlainText(content);
}

bool text_tab::get_fileSave(){
    return file_save;
}

void text_tab::set_fileSave(bool ifile_save){
    file_save = ifile_save;
}

std::string text_tab::get_path(){
    return path;
}

void text_tab::set_path(std::string ipath){
    path = ipath;
}

void text_tab::set_fontSize(int font_size){
    font.setPointSize(font_size);
    ui->plainTextEdit->setFont(font);
}
