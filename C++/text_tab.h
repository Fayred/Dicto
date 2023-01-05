#ifndef TEXT_TAB_H
#define TEXT_TAB_H

#include <QWidget>
#include <string>

namespace Ui {
class text_tab;
}

class text_tab : public QWidget
{
    Q_OBJECT

public:
    explicit text_tab(QWidget *parent = nullptr);
    ~text_tab();
    void set_fontSize(int);
    QString get_text();
    void set_text(QString);
    bool get_fileSave();
    void set_fileSave(bool);
    std::string get_path();
    void set_path(std::string);

private:
    Ui::text_tab *ui;
    bool file_save = false;
    std::string path;
    QFont font;
};

#endif // TEXT_TAB_H
