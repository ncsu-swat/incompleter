# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65940998/airflow-dag-serialization-typeerror-object-of-type-v1pod-is-not-json-seriali
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
...
_l_(416846)
volume_task = _c_(416867, _n_(416847, "PythonOperator", lambda: PythonOperator), task_id="task_with_volume",
            python_callable=_n_(416848, "test_volume_mount", lambda: test_volume_mount),
            executor_config={
                "pod_override": _c_(416866, _a_(416850, _n_(416849, "k8s", lambda: k8s), "V1Pod"), spec=_c_(416865, _a_(416852, _n_(416851, "k8s", lambda: k8s), "V1PodSpec"), containers=[
                            _c_(416858, _a_(416854, _n_(416853, "k8s", lambda: k8s), "V1Container"), name="base",
                                volume_mounts=[
                                    _c_(416857, _a_(416856, _n_(416855, "k8s", lambda: k8s), "V1VolumeMount"), mount_path="/foo/", name="example-kubernetes-test-volume"
                                    )
                                ],
                            )
                        ],
                        volumes=[
                            _c_(416864, _a_(416860, _n_(416859, "k8s", lambda: k8s), "V1Volume"), name="example-kubernetes-test-volume",
                                host_path=_c_(416863, _a_(416862, _n_(416861, "k8s", lambda: k8s), "V1HostPathVolumeSource"), path="/tmp/"),
                            )
                        ],
                    )
                ),
            },
        )
_l_(416868)
...
_l_(416869)