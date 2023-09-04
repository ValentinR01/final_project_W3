<script>
  import CircleIcon from "../../assets/icons/CircleIcon.svelte";

  import Icon from "../../components/atoms/Icon.svelte";
  import Text from "../../components/atoms/Text.svelte";
  import Rating from "../../components/molecules/Rating.svelte";
    
  /**
   * @type {{ asset: any[]; }}
  */
  export let data;
</script>

<div class="project-infos">
  <div class="w-100"> 
    <Text
      textTag='p'
      class='text-preset-4'
    >
      Nom du morceau : {data.asset[1].name}
    </Text>
  </div> 

  <div> 
    <Text
      textTag='p'
      class='text-preset-4'
    >
      Compositeur : {data.asset[1].name}
    </Text>
  </div> 

  <div> 
    <Text
      textTag='p'
      class='text-preset-4'
    >
      Epoque : {data.asset[1].name}
    </Text>
  </div> 

  <div> 
    <Text
      textTag='p'
      class='text-preset-4'
    >
      Catégorie : {data.asset[1].categorie}
    </Text>
  </div> 

  <div class="infos">
    <Text
      textTag='p'
      class='text-preset-4'
    >
      En ligne :
    </Text>
    {#if data.asset[1].published } 
      <Icon 
        name="circle" 
        width="12" 
        height="12" 
        color="var(--color-validation)"
      >
        <CircleIcon />
      </Icon>
    {:else}
      <Icon 
        name="circle" 
        width="12" 
        height="12" 
        color="var(--color-disabled)"
      >
        <CircleIcon />
      </Icon>
    {/if}
  </div>

  <div> 
    <Text
      textTag='p'
      class='text-preset-4'
    >
      Créé le : {data.asset[1].name}
    </Text>
  </div>

  <div> 
    <Text
      textTag='p'
      class='text-preset-4'
    >
      Filmé le : {data.asset[1].name}
    </Text>
  </div> 

  <div> 
    <Text
      textTag='p'
      class='text-preset-4 w-100'
    >
      Nom intervenant : {data.asset[1].name}
    </Text>
  </div> 

  {#if data.asset[1].categorie == "masterclass" }
    <div> 
      <Text
        textTag='p'
        class='text-preset-4'
      >
        Nom élève : {data.asset[1].name}
      </Text>
    </div>
  {/if}

  <div> 
    <Text
    textTag='p'
    class='text-preset-4'
    >
      Style de musique : {data.asset[1].name}
    </Text>
  </div> 

  <div> 
    <Text
    textTag='p'
    class='text-preset-4'
    >
      Instruments : {data.asset[1].instruments}
    </Text>
  </div> 

  <div> 
    <Text
    textTag='p'
    class='text-preset-4'
    >
      Langue de la vidéo : {data.asset[1].name}
    </Text>
  </div> 

  <div class="infos"> 
    <Text
    textTag='p'
    class='text-preset-4'
    >
      Niveau de difficulté :
    </Text>
    <Rating rate={data.asset[1].rating} />
  </div>

</div>

<style>
  .project-infos{
    display: flex;
    flex-wrap: wrap;
    row-gap: var(--spacing-3);
  }

  .infos{
    display: flex;
    column-gap: var(--spacing-1);
    align-items: center;
  }

  .project-infos > div{
    width: 50%;
  } 
  
</style>