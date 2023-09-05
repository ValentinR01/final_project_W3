<script>
  import ProjectInfosCard from '../../../../components/organisms/Cards/projectInfosCard.svelte';
  import Text from '../../../../components/atoms/Text.svelte';
  import Margin from '../../../../components/atoms/Margin.svelte';
  import Link from '../../../../components/atoms/Link.svelte';
  import CaptationApprovalForm from '../../../../components/organisms/Forms/CaptationApprovalForm.svelte';

  export let data;

  let step_lifecycle = 3;
  let captation_date = '26/08/2923';
  
</script>

<Margin marginTop='10%'>
  <div class='operator-details block-center'>
    <ProjectInfosCard data={data} />
  
    <div class="operator-management">
  
      <div class="card card--small">
        <Text
          textTag='h2'
          class='text-preset-2 text--uppercase text-center'
        >
          Date de captation
        </Text>

        {#if step_lifecycle = 3}
          <Margin marginTop='20px' marginBottom='10px'>
            <Text
              textTag='p'
              class='text-preset-4 text-center'
            >
              Capté le : {captation_date}
            </Text>
          </Margin>
            
          <CaptationApprovalForm />
        {:else}
          <Margin marginTop='20px' marginBottom='20px'>
            <Text
              textTag='p'
              class='text-preset-4 text-center'
            >
              Pas de créneau réservé pour l’instant
            </Text>
          </Margin>
  
          <Link linkUrl='/projects/operator/room-registration' linkColor='white' class='link--button'> Réserver créneau </Link>
        {/if}
      </div>
  
      <div class="card">
        <Text
          textTag='h2'
          class='text-preset-2 text--uppercase'
        >
          Commentaire
        </Text>
  
        <Margin marginTop='20px'>
          <Text
            textTag='p'
            class='text-preset-4'
          >
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a typ
          </Text>
        </Margin>
      </div>
  
    </div>
  
  </div>
</Margin>

<style>
  .operator-details{
    width: 60%;
    display: flex;
    flex-wrap: wrap;
  }

  .operator-details :global(.card-projectInfos){
    width: 100%;
  }

  .operator-management{
    display: flex;
    column-gap: var(--spacing-3);
    margin-top: var(--spacing-3);
  }

  .card--small{
    width: 35%;
  }
</style>