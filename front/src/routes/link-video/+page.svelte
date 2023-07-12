<script>
  import Text from '../../components/atoms/Text.svelte';
  import Image from '../../components/atoms/Image.svelte';
  import CommentaryCard from '../../components/molecules/cards/CommentaryCard.svelte';
  import CommentaryForm from '../../components/organisms/Forms/CommentaryForm.svelte';

  import Video from '../../assets/img/video_thumbnail.png';
  import Margin from '../../components/atoms/Margin.svelte';
  
  export let data;
  /**
   * @type {any}
   */
</script>

<div class='linkVideo-container'>
  <div class='card linkVideo__video block-center'>
    <Text
      textTag='h1'
      class='text-preset-2 text--uppercase'
      >
      Interview de Laura Sulob
    </Text>
  
    <Margin marginTop='var(--spacing-2)' marginBottom='var(--spacing-2)'>
      <Image
        imageSrc={Video}
        imageAlt="Saline Academie Logo"
        imageWidth=100%
        imageHeight=250
      />
    </Margin>

    <CommentaryForm userComment='new'/>
  
  </div>

  <div class='card linkVideo__comments block-center'>
    <Text
      textTag='h2'
      class='text-preset-2 text--uppercase'
      >
      Commentaires
    </Text>
  
    <CommentaryCard>
      <span slot='name'>{data.users[1].fullname}</span>
      <span slot='job'>{data.users[1].domain}</span>
      <span slot='date'> 12/06/2023 </span>
      <span slot='comment'> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. </span>
    </CommentaryCard>
    <CommentaryCard>
      <span slot='name'>{data.users[1].fullname}</span>
      <span slot='job'>{data.users[1].domain}</span>
      <span slot='date'> 12/06/2023 </span>
      <span slot='comment'> Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. </span>
    </CommentaryCard>
    <CommentaryCard>
      <span slot='name'>{data.users[1].fullname}</span>
      <span slot='job'>{data.users[1].domain}</span>
      <span slot='date'> 12/06/2023 </span>
      <span slot='comment'> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </span>
    </CommentaryCard>
  </div>
    
</div>

<style>
  .linkVideo-container{
    display: flex;
    column-gap: var(--spacing-3);
    margin: 0 var(--spacing-5);
  }

  .linkVideo__video{
    height: 68vh;
  }

  .linkVideo__comments{
    width: 30%;
    padding: var(--spacing-4) var(--spacing-4);
    display: flex;
    flex-wrap: wrap;
    row-gap: var(--spacing-3);
    overflow: scroll;
    height: 68vh;
  }
</style>