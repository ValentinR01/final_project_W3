<script>
  import DownloadIcon from "../../assets/icons/DownloadIcon.svelte";
  import ShareIcon from "../../assets/icons/ShareIcon.svelte";

  import Button from "../../components/atoms/Button.svelte";
  import Margin from "../../components/atoms/Margin.svelte";
  import Text from "../../components/atoms/Text.svelte";
  import VideoAction from "../../components/molecules/cards/VideoAction.svelte";
</script>

<div class="video-actions">
  <VideoAction>
    <DownloadIcon slot='icon' />
    <span slot='text'>Télécharger la vidéo</span>
  </VideoAction>

  <VideoAction>
    <ShareIcon slot='icon' />
    <span slot='text'>Partager la vidéo</span>
  </VideoAction>
</div>

<Margin marginTop="var(--spacing-4)">
  <Text
    textTag='p'
    class='text-preset-4 text-center'
  >
    Phase : 
  </Text>
</Margin>

<form>
  <Button marginTop='var(--spacing-3)'> Valider </Button>
  <Button class='button--secondary' marginTop='var(--spacing-3)'> Refuser </Button>
</form>

<style>
  .video-actions{
    display: flex;
    column-gap: var(--spacing-3);
  }

  form{
    display: flex;
    justify-content: center;
    column-gap: var(--spacing-2);
  }
</style>