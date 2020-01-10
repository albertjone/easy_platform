# working progress
 - parse args
 - logger module

# features
## devstack
### all-in-one

### multinode

## kubernetes

### all-in-one


### multinode


## utils

### images
  * action
    - pull
      - you can appoint your registry
        - --registry
      - you can download all tags
        - --all-tags , -a
      - you can skip image verification
        - --disable-content-trust
      - you set platform if server is multi-platform capable
        - --platform	
      - you can appoint your image download directory
        - --image-pull-dir
      - you can decide what images you need to download by a yaml file
        - --image-pull-yaml-file
    - push
      - you can appoint your registry
        - --registry
      - you can appoint your image upload directory
        - --image-push-dir
      - you can decide what images you need to download by a yaml file
        - --image-push-yaml-file
    - build
      - you can appoint your registry
        - --registry
      - you can appoint your image build directorys
        - --image-build-dir
      - you can decide what image you want to build by a yaml file
        - --image-build-yaml-file