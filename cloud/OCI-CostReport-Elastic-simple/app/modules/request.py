#!/usr/bin/env python
# -*- coding: utf-8 -*-

def RequestDownload(client, bucket, prefix, path):
    '''
    Descarga los files de costos desde OCI 
    Parameters
    ----------
    client : oci obj
        obj con la configuracion de OCI
    bucket: str
        nombre del bucket
    start: str
        nombre de file desde donde empezar las descargas (excluye)
    end: str
        nombre de file donde finalizar las descargas (excluye)
    path: str
        directorio donde se guardaran las descargas
    Returns
    ---------
    list
    '''
    namespace = 'bling'
    report_bucket_objects = client.list_objects(namespace_name=namespace,
                                                bucket_name=bucket,
                                                prefix=prefix)

    list_name = []
    for i in report_bucket_objects.data.objects:
        filename = i.name
        object_details = client.get_object(namespace_name=namespace,
                                           bucket_name=bucket,
                                           object_name=i.name)

        print('Descargando desde: ', filename)
        with open(path+filename.rsplit('/', 1)[-1], 'wb') as f:
            for chunk in object_details.data.raw.stream(2048 ** 2, decode_content=False):
                f.write(chunk)
        
        list_name.append(filename)

    return list_name