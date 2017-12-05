mispTypesMapping = {
    'vulnerability': {'source_name': 'cve', 'external_id': ''},
    'md5': {'observable': {'0': {'type': 'file', 'hashes': ''}},
            'pattern': 'file:hashes.\'md5\' = \'{0}\''},
    'sha1': {'observable': {'0': {'type': 'file', 'hashes': ''}},
             'pattern': 'file:hashes.\'sha1\' = \'{0}\''},
    'sha256': {'observable': {'0': {'type': 'file', 'hashes': ''}},
               'pattern': 'file:hashes.\'sha256\' = \'{0}\''},
    'filename': {'observable': {'0': {'type': 'file', 'name': ''}},
                 'pattern': 'file:name = \'{0}\''},
    'filename|md5': {'observable': {'0': {'type': 'file', 'name': '', 'hashes': ''}},
                     'pattern': 'file:name = \'{0}\' AND file:hashes.\'md5\' = \'{1}\''},
    'filename|sha1': {'observable': {'0': {'type': 'file', 'name': '', 'hashes': ''}},
                      'pattern': 'file:name = \'{0}\' AND file:hashes.\'sha1\' = \'{1}\''},
    'filename|sha256': {'observable': {'0': {'type': 'file', 'name': '', 'hashes': ''}},
                        'pattern': 'file:name = \'{0}\' AND file:hashes.\'sha256\' = \'{1}\''},
    'ip-src': {'observable': {'0': {'type': '', 'value': ''}},
               'pattern': '{0}:value = \'{1}\''},
    'ip-dst': {'observable': {'0': {'type': '', 'value': ''}},
               'pattern': '{0}:value = \'{1}\''},
    'hostname': {'observable': {'0': {'type': 'domain-name', 'value': ''}},
                 'pattern': 'domain-name:value = \'{0}\''},
    'domain': {'observable': {'0': {'type': 'domain-name', 'value': ''}},
               'pattern': 'domain-name:value = \'{0}\''},
    'domain|ip': {'observable': {'0': {'type': 'domain-name', 'value': '', 'resolves_to_refs': '1'}, '1': {'type': '', 'value': ''}},
                  'pattern': 'domain-name:value = \'{0}\' AND domain-name:resolves_to_refs[*].value = \'{1}\''},
    'email-src': {'observable': {'0': {'type': 'email-addr', 'value': ''}},
                  'pattern': 'email-addr:value = \'{0}\''},
    'email-dst': {'observable': {'0': {'type': 'email-addr', 'value': ''}},
                  'pattern': 'email-addr:value = \'{0}\''},
    'email-subject': {'observable': {'0': {'type': 'email-message', 'subject': '', 'is_multipart': 'false'}},
                      'pattern': 'email-message:subject = \'{0}\''},

    'email-body': {'observable': {'0': {'type': 'email-message', 'body': '', 'is_multipart': 'false'}},
                   'pattern': 'email-message:body = \'{0}\''},
    'url': {'observable': {'0': {'type': 'url', 'value': ''}},
            'pattern': 'url:value = \'{0}\''},
    'regkey': {'observable': {'0': {'type': 'windows-registry-key', 'key': ''}},
               'pattern': 'windows-registry-key:key = \'{0}\''},
    'regkey|value': {'observable': {'0': {'type': 'windows-registry-key', 'key': '', 'values': {'name': ''}}},
                     'pattern': 'windows-registry-key:key = \'{0}\' AND windows-registry-key:values = \'{1}\''},
    'malware-sample': {'observable': {'0': {'type': 'file', 'name': '', 'hashes': ''}},
                       'pattern': 'file:name = \'{0}\' AND file:hashes.\'md5\' = \'{1}\''},
    'mutex': {'observable': {'0': {'type': 'mutex', 'name': ''}},
              'pattern': 'mutex:name = \'{0}\''},
    'uri': {'observable': {'0': {'type': 'url', 'value': ''}},
            'pattern': 'url:value = \'{0}\''},
    'authentihash': {'observable': {'0': {'type': 'file', 'hashes': ''}},
                     'pattern': 'file:hashes.\'authentihash\' = \'{0}\''},
    'ssdeep': {'observable': {'0': {'type': 'file', 'hashes': ''}},
               'pattern': 'file:hashes.\'ssdeep\' = \'{0}\''},
    'imphash': {'observable': {'0': {'type': 'file', 'hashes': ''}},
                'pattern': 'file:hashes.\'imphash\' = \'{0}\''},
    'pehash': {'observable': {'0': {'type': 'file', 'hashes': ''}},
               'pattern': 'file:hashes.\'pehash\' = \'{0}\''},
    'impfuzzy': {'observable': {'0': {'type': 'file', 'hashes': ''}},
                 'pattern': 'file:hashes.\'impfuzzy\' = \'{0}\''},
    'sha224': {'observable': {'0': {'type': 'file', 'hashes': ''}},
               'pattern': 'file:hashes.\'sha224\' = \'{0}\''},
    'sha384': {'observable': {'0': {'type': 'file', 'hashes': ''}},
               'pattern': 'file:hashes.\'sha384\' = \'{0}\''},
    'sha512': {'observable': {'0': {'type': 'file', 'hashes': ''}},
               'pattern': 'file:hashes.\'sha512\' = \'{0}\''},
    'sha512/224': {'observable': {'0': {'type': 'file', 'hashes': ''}},
                   'pattern': 'file:hashes.\'sha512/224\' = \'{0}\''},
    'sha512/256': {'observable': {'0': {'type': 'file', 'hashes': ''}},
                   'pattern': 'file:hashes.\'sha512/256\' = \'{0}\''},
    'tlsh': {'observable': {'0': {'type': 'file', 'hashes': ''}},
             'pattern': 'file:hashes.\'tlsh\' = \'{0}\''},
    'filename|authentihash': {'observable': {'0': {'type': 'file', 'name': '', 'hashes': ''}},
                              'pattern': 'file:name = \'{0}\' AND file:hashes.\'authentihash\' = \'{1}\''},
    'filename|ssdeep': {'observable': {'0': {'type': 'file', 'name': '', 'hashes': ''}},
                        'pattern': 'file:name = \'{0}\' AND file:hashes.\'ssdeep\' = \'{1}\''},
    'filename|imphash': {'observable': {'0': {'type': 'file', 'name': '', 'hashes': ''}},
                         'pattern': 'file:name = \'{0}\' AND file:hashes.\'imphash\' = \'{1}\''},
    'filename|impfuzzy': {'observable': {'0': {'type': 'file', 'name': '', 'hashes': ''}},
                          'pattern': 'file:name = \'{0}\' AND file:hashes.\'impfuzzy\' = \'{1}\''},
    'filename|pehash': {'observable': {'0': {'type': 'file', 'name': '', 'hashes': ''}},
                        'pattern': 'file:name = \'{0}\' AND file:hashes.\'pehash\' = \'{1}\''},
    'filename|sha224': {'observable': {'0': {'type': 'file', 'name': '', 'hashes': ''}},
                        'pattern': 'file:name = \'{0}\' AND file:hashes.\'sha224\' = \'{1}\''},
    'filename|sha384': {'observable': {'0': {'type': 'file', 'name': '', 'hashes': ''}},
                        'pattern': 'file:name = \'{0}\' AND file:hashes.\'sha384\' = \'{1}\''},
    'filename|sha512': {'observable': {'0': {'type': 'file', 'name': '', 'hashes': ''}},
                        'pattern': 'file:name = \'{0}\' AND file:hashes.\'sha512\' = \'{1}\''},
    'filename|sha512/224': {'observable': {'0': {'type': 'file', 'name': '', 'hashes': ''}},
                            'pattern': 'file:name = \'{0}\' AND file:hashes.\'sha512/224\' = \'{1}\''},
    'filename|sha512/256': {'observable': {'0': {'type': 'file', 'name': '', 'hashes': ''}},
                            'pattern': 'file:name = \'{0}\' AND file:hashes.\'sha512/256\' = \'{1}\''},
    'filename|tlsh': {'observable': {'0': {'type': 'file', 'name': '', 'hashes': ''}},
                      'pattern': 'file:name = \'{0}\' AND file:hashes.\'tlsh\' = \'{1}\''},
    'x509-fingerprint-sha1': {'observable': {'0': {'type': 'x509-certificate', 'hashes': {'sha1': ''}}},
                              'pattern': 'x509-certificate:hashes = \'{0}\''},
    'port': {'observable': {'0': {'type': 'network-traffic', 'dst_port': '', 'protpocols': []}},
             'pattern': 'network-traffic:dst_port = \'{0}\''},
    'ip-dst|port': {'observable': {'0': {'type': '', 'value': ''}, '1': {'type': 'network-traffic', 'dst_ref': '0', 'dst_port': '', 'protocols': []}},
                    'pattern': 'network-traffic:dst_port = \'{1}\' AND network-traffic:dst_ref.type = \'{2}\' AND network-traffic:dst_ref.value = \'{0}\''},
    'ip-src|port': {'observable': {'0': {'type': '', 'value': ''}, '1': {'type': 'network-traffic', 'src_ref': '0', 'dst_port': '', 'protocols': []}},
                    'pattern': 'network-traffic:src_port = \'{1}\' AND network-traffic:src_ref.type = \'{2}\' AND network-traffic:src_ref.value = \'{0}\''},
    'hostname|port': {'observable': {'0': {'type': 'domain-name', 'value': ''}, '1': {'type': 'network-traffic', 'dst_ref': '0', 'dst_port': '', 'protocols': []}},
                      'pattern': 'domain-name:value = \'{0}\' AND network-traffic:dst_port = \'{1}\''},
    'email-dst-display-name': {'observable': {'0': {'type': 'email-addr', 'display_name': ''}},
                               'pattern': 'email-addr:display_name = \'{0}\''},
    'email-src-display-name': {'observable': {'0': {'type': 'email-addr', 'display_name': ''}},
                               'pattern': 'email-addr:display_name = \'{0}\''},
    'email-reply-to': {'observable': {'0': {'type': 'email-addr', 'value': ''}},
                       'pattern': 'email-addr:value = \'{0}\''},
    'attachment': {'observable': {'0': {'type': 'artifact', 'payload_bin': ''}},
                   'pattern': 'artifact:payload_bin = \'{0}\''},
    'mac-address': {'observable': {'0': {'type': 'mac-addr', 'value': ''}},
                    'pattern': 'mac-addr:value = \'{0}\''}
}

objectsMapping = {'domain|ip': {'pattern': 'domain-name:{0} = \'{1}\' AND '},
                 'email': {'observable': {'0': {'type': 'email-message'}},
                           'pattern': 'email-{0}:{1} = \'{2}\' AND '},
                 'file': {'observable': {'0': {'type': 'file', 'hashes': {}}},
                          'pattern': 'file:{0} = \'{1}\' AND '},
                 'ip|port': {'pattern': 'network-traffic:{0} = \'{1}\' AND '},
                 'registry-key': {'observable': {'0': {'type': 'windows-registry-key'}},
                                  'pattern': 'windows-registry-key:{0} = \'{1}\' AND '},
                 'url': {'observable': {'0': {'type': 'url'}},
                         'pattern': 'url:{0} = \'{1}\' AND '},
                 'x509': {'observable': {'0': {'type': 'x509-certificate', 'hashes': {}}},
                          'pattern': 'x509-certificate:{0} = \'{1}\' AND '}
}
relationshipsSpecifications = {'attack-pattern': {'vulnerability': 'targets', 'identity': 'targets',
                                                 'malware': 'uses', 'tool': 'uses'},
                              'campaign': {'intrusion-set': 'attributed-to', 'threat-actor': 'attributed-to',
                                           'identity': 'targets', 'vulnerability': 'targets',
                                           'attack-pattern': 'uses', 'malware': 'uses',
                                           'tool': 'uses'},
                              'course-of-action':{'attack-pattern': 'mitigates', 'malware': 'mitigates',
                                                  'tool': 'mitigates', 'vulnerability': 'mitigates'},
                              'indicator': {'attack-pattern': 'indicates', 'cacmpaign': 'indicates',
                                            'intrusion-set': 'indicates', 'malware': 'indicates',
                                            'threat-actor': 'indicates', 'tool': 'indicates'},
                              'intrusion-set': {'threat-actor': 'attributed-to', 'identity': 'targets',
                                                'vulnerability': 'targets', 'attack-pattern': 'uses',
                                                'malware': 'uses', 'tool': 'uses'},
                              'malware': {'identity': 'targets', 'vulnerability': 'targets',
                                          'tool': 'uses', 'malware': 'variant-of'},
                              'threat-actor': {'identity': 'attributed-to', 'vulnerability': 'targets',
                                               'attack-pattern': 'uses', 'malware': 'uses',
                                               'tool': 'uses'},
                              'tool': {'identity': 'targets', 'vulnerability': 'targets'}
}
objectTypes = {'text': {'x509': {'subject': 'subject', 'issuer': 'issuer', 'pubkey-info-algorithm': 'subject_public_key_algorithm',
                                'pubkey-info-exponent': 'subject_public_key_exponent', 'pubkey-info-modulus': 'subject_public_key_modulus',
                                'serial-number': 'serial_number', 'version': 'version'},
                       'file': {'mimetype': 'mime_type'}},
              'datetime': {'x509': {'validity-not-before': 'validity_not_before', 'validity-not-after': 'validity_not_after'},
                           'ip|port': {'first-seen': 'start', 'last-seen': 'end'},
                           'email': 'date',
                           'registry-key': 'modified'},
              'port': {'src-port': 'src_port', 'dst-port': 'dst_port'}, 'url': 'value',
              'domain': {'domain': 'domain'}, 'email-x-mailer': 'additional_header_fields.X-Mailer',
              'email-subject': 'subject', 'email-attachment': 'body_multipart[*].body_raw_ref.name',
              'email-dst': {'to': 'to_refs', 'cc': 'cc_refs'}, 'email-src': 'from_ref',
              'email-reply-to': 'additional_header_fields.Reply-To',
              'hashes': 'hashes.\'{0}\'', 'size-in-bytes': 'size', 'filename': 'name',
              'ip-dst': {'ip|port': 'dst_ref.type = \'{0}\' AND network-traffic:dst_ref.value',
                         'domain|ip': 'resolves_to_refs[*].value'},
              'reg-datatype': 'datatype', 'reg-data': 'data', 'reg-name': 'name', 'reg-key': 'key'
}

defineProtocols = {'80': 'http', '443': 'https'} 
