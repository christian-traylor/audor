#include <gtk/gtk.h>
#include <stdio.h>
#include <stdlib.h>

void on_file_selected(GtkWidget *widget, gpointer data) {
    GtkFileChooser *chooser = GTK_FILE_CHOOSER(widget);
    char *file_path = gtk_file_chooser_get_filename(chooser);
    
    if (file_path != NULL) {
        char command[256];
        snprintf(command, sizeof(command), "python3 ../audor/detect.py \"%s\"", file_path);
        int result = system(command);
        if (result != 0) {
            perror("Error executing Python script");
        }
        g_free(file_path);
    }
}

void on_button_clicked(GtkWidget *widget, gpointer data) {
    GtkWidget *dialog = gtk_file_chooser_dialog_new("Open File",
                                                    GTK_WINDOW(data),
                                                    GTK_FILE_CHOOSER_ACTION_OPEN,
                                                    "_Cancel", GTK_RESPONSE_CANCEL,
                                                    "_Open", GTK_RESPONSE_ACCEPT,
                                                    NULL);
    if (gtk_dialog_run(GTK_DIALOG(dialog)) == GTK_RESPONSE_ACCEPT) {
        on_file_selected(GTK_WIDGET(dialog), data);
    }
    gtk_widget_destroy(dialog);
}

int main(int argc, char *argv[]) {
    GtkWidget *window;
    GtkWidget *button;
    GtkWidget *vbox;

    gtk_init(&argc, &argv);

    window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(window), "Audor");
    gtk_window_set_default_size(GTK_WINDOW(window), 300, 200);
    gtk_window_set_position(GTK_WINDOW(window), GTK_WIN_POS_CENTER);
    g_signal_connect(window, "destroy", G_CALLBACK(gtk_main_quit), NULL);

    vbox = gtk_box_new(GTK_ORIENTATION_VERTICAL, 5);
    gtk_container_add(GTK_CONTAINER(window), vbox);

    button = gtk_button_new_with_label("Select File");
    gtk_box_pack_start(GTK_BOX(vbox), button, FALSE, FALSE, 0);

    g_signal_connect(button, "clicked", G_CALLBACK(on_button_clicked), window);

    gtk_widget_show_all(window);

    gtk_main();

    return 0;
}