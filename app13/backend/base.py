import reflex as rx


class States(rx.States):
    def get_image_path(self, id_image) -> str:
        if id_image is None:
            return "/nophoto.jpg"

        image_id_str = str(id_image)
        lista_digitos = list(image_id_str)
        image_path = 'https://quinchau.com/webmaster2/weberp/img/p/' + \
            '/'.join(lista_digitos) + "/" + image_id_str + ".jpg"
        return image_path
