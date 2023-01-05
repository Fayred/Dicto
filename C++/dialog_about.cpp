#include "dialog_about.h"
#include "ui_dialog_about.h"

dialog_about::dialog_about(QWidget *parent) : QDialog(parent), ui(new Ui::dialog_about)
{
    ui->setupUi(this);
}

dialog_about::~dialog_about()
{
    delete ui;
}

void dialog_about::on_close_button_clicked()
{
   this->close();
}

