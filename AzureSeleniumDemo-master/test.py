trigger:
- master

pool:
  vmImage: 'windows-latest'

variables:
  buildConfiguration: 'Release'

stages:
  - stage: 
    displayName: Build
    jobs:
    - job: build
      steps:
        - task: ArchiveFiles@2
          displayName: 'Archive files'
          inputs:
            rootFolderOrFile: '$(Build.SourcesDirectory)'
            includeRootFolder: false
            archiveType: 'zip'
            archiveFile: '$(Build.ArtifactStagingDirectory)/web-app.zip'
            replaceExistingArchive: true

        - publish: $(Build.ArtifactStagingDirectory)
          artifact: web-app 


  - stage: 
    displayName: Selenium Testing
    jobs:
    - job: selenium_tests
      displayName: Run Selenium Tests
      steps:
        - task: UsePythonVersion@0
          inputs:
            versionSpec: '3.x'

        - script: |
            pip install selenium
          displayName: 'Install Selenium'
                
        - script: |
            pip install webdriver_manager
          displayName: 'Install webdriver_manager'
        
        - script: |
            python tests.py
          displayName: 'Run Selenium Tests'




  
