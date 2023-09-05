<script>
  import UploadIcon from "../../../../assets/icons/UploadIcon.svelte";
  import DownloadIcon from "../../../../assets/icons/DownloadIcon.svelte";
  import FileAction from "../../../../components/atoms/FileAction.svelte";

  import CommentariesCard from "../../../../components/organisms/Cards/commentariesCard.svelte";
  import ProjectInfosCard from "../../../../components/organisms/Cards/projectInfosCard.svelte";

  export let data;
</script>

<div class='postprod-details block-center'>
  <ProjectInfosCard data={data} />

  <div class='actions-postProd block-center'>
    <FileAction action='download' nameInput='file'>
      <DownloadIcon slot='icon' />
      <span slot='text'> TÉLÉCHARGER LA VIDÉO MONTÉE </span>  
    </FileAction> 
     
    <FileAction action='upload' nameInput='file'>
      <UploadIcon slot='icon' />
      <span slot='text'> UPLOADER FICHIER TRADUCTION </span>  
    </FileAction>
  
  </div>
  
  <CommentariesCard data={data} />
</div>

<style>
  .postprod-details{
    width: 60%;
    margin-top: 3%;
  }
  
  .postprod-details :global(.card){
    width: auto;
  }

  .actions-postProd{
    width: 100%;
    display: flex;
    justify-content: center;
    column-gap: var(--spacing-2);
  }

  .actions-postProd :global(.file-action){
    margin-top: var(--spacing-2);
    width: 50%;
  }
</style>