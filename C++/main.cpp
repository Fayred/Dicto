#include "dicto.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    dicto w;
    w.show();
    return a.exec();
}
